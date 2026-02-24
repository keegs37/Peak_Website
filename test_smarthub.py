import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Starting Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            print("Navigating to Shop.html...")
            await page.goto("https://peak.smarthub.coop/Shop.html", wait_until="domcontentloaded")
            print("Waiting for Street Address label...")
            await page.wait_for_selector("text=Street Address", timeout=35000)
            
            print("Filling address box...")
            input_el = page.locator("input.gwt-TextBox").first
            await input_el.fill("100 Main St", force=True, timeout=10000)
            await input_el.press("Enter")
            await input_el.press("Tab")
            await asyncio.sleep(1)
            print("Filled first input")
            
            print("Clicking Go! by text...")
            go_button = page.locator("button.btn-primary:has-text('Go!')").first
            await go_button.click(force=True, timeout=5000)
            print("Clicked Go!")
            
            await asyncio.sleep(3)
            await page.screenshot(path="smarthub_success.png", full_page=True)
            print("Screenshot saved")
            
        except Exception as e:
            print(f"Error: {e}")
            await page.screenshot(path="smarthub_error3.png", full_page=True)
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
