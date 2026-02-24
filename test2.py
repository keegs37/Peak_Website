import asyncio
from playwright.async_api import async_playwright
import re

async def main():
    address = "1900 West Oak Street, Lebanon, OR 97355, USA"
    parts = [p.strip() for p in address.split(',')]
    street = parts[0]
    city = parts[1]
    state_zip = parts[2].split()
    state = state_zip[0]
    
    state_mapping = {
        'OR': 'Oregon',
        'WA': 'Washington',
        'CA': 'California',
        'ID': 'Idaho'
    }
    state_label = state_mapping.get(state.upper(), state)

    print(f"Parsed: Street={street}, City={city}, State={state_label}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            print("Navigating to Shop.html...")
            await page.goto("https://peak.smarthub.coop/Shop.html", wait_until="domcontentloaded")
            await page.wait_for_selector("text=Street Address", timeout=35000)
            
            print("Form loaded. Selecting state...")
            state_select = page.locator("select.form-control").nth(0)
            await state_select.select_option(label=state_label)
            
            await asyncio.sleep(1) # wait for city to populate
            print("Selecting city...")
            city_select = page.locator("select.form-control").nth(1)
            
            # SmartHub might take time to fetch cities
            # We can wait until the city option is available
            await city_select.wait_for(state="attached")
            
            # Select the option
            await city_select.select_option(label=city)
            
            await asyncio.sleep(1)
            print("Filling street...")
            street_input = page.locator("input.gwt-SuggestBox.form-control").first
            await street_input.fill(street)
            
            print("Clicking Go!...")
            go_button = page.locator("button.btn-primary:has-text('Go!')").first
            await go_button.click()
            
            print("Waiting for verification list or next step...")
            await asyncio.sleep(4)
            await page.screenshot(path="step1.png", full_page=True)
            
            # The subagent mentioned: "Clicked the 'Go!' button after selecting the verified address."
            # We might need to click Go again.
            verify_go_button = page.locator("button.btn-primary:has-text('Go!')").nth(1)
            if await verify_go_button.is_visible():
                print("Clicking Second Go!...")
                await verify_go_button.click()
                await asyncio.sleep(4)
                await page.screenshot(path="step2.png", full_page=True)
            else:
                # maybe the first button is still the only one, or dialogue popped up
                print("Second Go! not visible, checking dialogs")
                pass
            
            print("Checking final result...")
            try:
                result_text = await page.locator(".gwt-DialogBox").inner_text(timeout=3000)
                print("Dialog Text:", result_text)
            except:
                print("No dialog box found. Getting body text...")
                body_text = await page.locator("body").inner_text()
                if "What kind of services are you looking for?" in body_text:
                    print("SUCCESS! Reached the interest form.")
                else:
                    print("Could not verify success. Here is some body text:", body_text[:500])
                    
        except Exception as e:
            print(f"Error: {e}")
            await page.screenshot(path="error.png", full_page=True)
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
