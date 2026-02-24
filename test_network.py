import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Intercept network requests
        async def handle_request(route, request):
            if request.method == "POST" and "smarthub" in request.url:
                print(f"Intercepted Request URL: {request.url}")
                print(f"Headers: {request.headers}")
                print(f"Post Data: {request.post_data}")
            await route.continue_()

        await page.route("**/*", handle_request)
        
        try:
            print("Navigating to Shop.html...")
            await page.goto("https://peak.smarthub.coop/Shop.html", wait_until="domcontentloaded")
            await page.wait_for_selector("text=Street Address", timeout=35000)
            
            # Form elements
            state_select = page.locator("select.form-control").nth(0)
            await state_select.wait_for(state="attached", timeout=20000)
            await state_select.select_option(label="Oregon", timeout=20000)
            await asyncio.sleep(2)
            
            city_select = page.locator("select.form-control").nth(1)
            await city_select.wait_for(state="attached", timeout=20000)
            await city_select.select_option(label="Lebanon", timeout=20000)
            await asyncio.sleep(2)

            
            street_input = page.locator("input.gwt-SuggestBox.form-control").first
            await street_input.fill("1900 West Oak Street")
            
            print("Clicking Go!...")
            go_button = page.locator("button.btn-primary:has-text('Go!')").first
            await go_button.click()
            
            await asyncio.sleep(5)
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
