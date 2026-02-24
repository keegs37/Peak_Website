from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from playwright.async_api import async_playwright
import uvicorn
import asyncio
import os
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Playwright state for Browser Pool Optimization
pw = None
browser = None

@app.on_event("startup")
async def startup_event():
    global pw, browser
    pw = await async_playwright().start()
    # Keep one headless browser instance running permanently in the background
    browser = await pw.chromium.launch(headless=True)
    print("Background browser pool started.")
    
@app.on_event("shutdown")
async def shutdown_event():
    global pw, browser
    if browser:
        await browser.close()
    if pw:
        await pw.stop()
    print("Background browser pool stopped.")

@app.get("/api/check")
async def check_availability(address: str):
    if not address:
        raise HTTPException(status_code=400, detail="Address is required")

    # Parse address parts
    parts = [p.strip() for p in address.replace('\n', ', ').split(',')]
    if len(parts) >= 3:
        street = parts[0]
        city = parts[1]
        state_zip = parts[2].split()
        state = state_zip[0] if state_zip else "OR"
    else:
        m = re.search(r'^(.*?)\s+([A-Za-z]+)[,\s]+([A-Za-z]{2})\s*(\d{5})?.*$', address)
        if m:
            street = m.group(1).strip()
            city = m.group(2).strip()
            state = m.group(3).strip()
        else:
            street = address
            city = ""
            state = "OR"
        
    state_mapping = {'OR': 'Oregon', 'WA': 'Washington', 'CA': 'California', 'ID': 'Idaho'}
    state_label = state_mapping.get(state.upper(), "Oregon")

    try:
        page = await browser.new_page()
        
        # Load the page to ensure we have the nocache tokens and JSESSIONID
        await page.goto("https://peak.smarthub.coop/Shop.html", wait_until="domcontentloaded")
        
        # We need the RPC hash and permutation... but wait! We can just use the playwright network interception
        # to capture the real payload it generates when we type anything, replace the address string, and send it back!
        
        # Setup the interceptor to catch the MemberService request, swap the address, and resume
        search_str = street if street else address
        
        captured_response = None
        
        async def intercept_request(route, request):
            nonlocal captured_response
            if request.method == "POST" and "gwt/MemberService" in request.url:
                post_data = request.post_data
                if post_data and "getAddressForMember" in post_data:
                    # GWT payloads encode strings. We will find "1900 West Oak Street" or whatever we typed
                    # and replace it with our target search_str
                    # But actually we can just type the TARGET search_str in the UI directly and we don't even need to replace!
                    pass
            await route.continue_()
            
        await page.route("**/*", intercept_request)
        
        # Now just fill the form normally in Playwright. 
        # But wait, earlier we found Playwright was timing out on the form fields because of GWT.
        # Let's fix the form interaction to be perfectly reliable.
        
        # 1. Wait for page to settle
        await asyncio.sleep(1)
        
        # 2. Select state using JavaScript to bypass flaky UI
        await page.evaluate(f'''() => {{
            const selects = document.querySelectorAll('select');
            if(selects.length > 0) {{
                // Find Oregon option
                const opts = Array.from(selects[0].options);
                const targetOpt = opts.find(o => o.text.includes('{state_label}'));
                if(targetOpt) {{
                    selects[0].value = targetOpt.value;
                    selects[0].dispatchEvent(new Event('change', {{ bubbles: true }}));
                }}
            }}
        }}''')
        
        await asyncio.sleep(0.5)
        
        # 3. Select city using JavaScript
        if city:
            await page.evaluate(f'''() => {{
                const selects = document.querySelectorAll('select');
                if(selects.length > 1) {{
                    const opts = Array.from(selects[1].options);
                    const targetOpt = opts.find(o => o.text.includes('{city}'));
                    if(targetOpt) {{
                        selects[1].value = targetOpt.value;
                        selects[1].dispatchEvent(new Event('change', {{ bubbles: true }}));
                    }}
                }}
            }}''')
            
        await asyncio.sleep(0.5)
        
        # 4. Fill street
        input_el = page.locator("input.gwt-SuggestBox.form-control").first
        await input_el.fill(street, force=True)
        await input_el.press("Enter")
        await input_el.press("Tab")
        
        # Click Go and wait for response simultaneously
        try:
            go_button = page.locator("button.btn-primary:has-text('Go!')").first
            
            # Start waiting for the network response before clicking
            async def verify_gwt_response(response):
                return response.request.method == "POST" and "MemberService" in response.url
                
            async with page.expect_response(verify_gwt_response, timeout=10000) as response_info:
                await go_button.click(force=True, timeout=5000)
                print("Clicked Go Button via Playwright")
                
            response = await response_info.value
            captured_response = await response.text()
            print("Captured Response length:", len(captured_response))
            
        except Exception as e:
            print("Failed to click Go Button or timed out waiting for response:", e)
            try:
                # Start wait again for JS fallback
                async def verify_gwt_response(response):
                    return response.request.method == "POST" and "MemberService" in response.url
                    
                async with page.expect_response(verify_gwt_response, timeout=10000) as response_info:
                    await page.evaluate('''() => {
                        const btns = Array.from(document.querySelectorAll('button'));
                        const goBtn = btns.find(b => b.textContent.includes('Go!'));
                        if(goBtn) goBtn.click();
                    }''')
                    print("Clicked Go Button via JS")
                    
                response = await response_info.value
                captured_response = await response.text()
            except Exception as e2:
                print("JS Click also failed:", e2)
                return {"status": "error", "message": "Submit button not found or network timed out."}
                
        # Address matching verify list (a second Go button becomes visible for fuzzy matches)
        await asyncio.sleep(2)
        try:
            verify_go_buttons = page.locator("button.btn-primary:has-text('Go!')")
            count = await verify_go_buttons.count()
            for i in range(count):
                btn = verify_go_buttons.nth(i)
                if await btn.is_visible() and await btn.is_enabled():
                    # We could also wait for response here, but usually the first response gave us standard GWT OK array
                    await btn.click(force=True, timeout=3000)
                    print("Clicked secondary Go button for verify list")
                    await asyncio.sleep(2)
        except:
            pass
            
        if captured_response:
            if captured_response.startswith("//OK"):
                if "addresses" in captured_response.lower() or "zip" in captured_response.lower():
                     return {"status": "success", "message": "Address found and verified by SmartHub!"}
                else:
                     return {"status": "success", "message": "Address verified!"}
            else:
                return {"status": "error", "message": "SmartHub could not verify this address, or more specific City/State filtering is required."}
        else:
             return {"status": "error", "message": f"Network error from SmartHub or request timed out"}
            
    except Exception as e:
        print("API unhandled exception:", e)
        return {"status": "error", "message": "An internal error occurred while validating the address."}
    finally:
        try:
            # We must gracefully close the page or memory leaks will crush the server
            await page.close()
        except:
            pass

current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount("/", StaticFiles(directory=current_dir, html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)

