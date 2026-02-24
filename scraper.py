import asyncio
import json
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TOKEN_FILE = "smarthub_tokens.json"

async def scrape_tokens():
    logging.info("Starting background token scraper...")
    tokens = {
        "jsessionid": None,
        "xsrf_token": None,
        "permutation": None,
        "rpc_hash": None,
    }
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        async def handle_request(route, request):
            if request.method == "POST" and "gwt/MemberService" in request.url:
                # payload looks like: 7|0|4|https://peak.smarthub.coop/|B594...|coop...|getAddressForMember|1|2|3|4|0|
                post_data = request.post_data
                if post_data and "getAddressForMember" in post_data:
                    parts = post_data.split('|')
                    if len(parts) > 5:
                        tokens["rpc_hash"] = parts[4]
                        logging.info(f"Captured RPC Hash: {tokens['rpc_hash']}")
                
                # capture headers
                headers = request.headers
                if 'x-gwt-permutation' in headers:
                    tokens["permutation"] = headers['x-gwt-permutation']
                    logging.info(f"Captured Permutation: {tokens['permutation']}")
                    
            await route.continue_()

        await page.route("**/*", handle_request)
        
        try:
            logging.info("Navigating to Shop.html to generate tokens...")
            await page.goto("https://peak.smarthub.coop/Shop.html", wait_until="domcontentloaded")
            await page.wait_for_selector("text=Street Address", timeout=35000)
            
            # Extract cookies
            context = page.context
            cookies = await context.cookies()
            for cookie in cookies:
                if cookie['name'] == 'JSESSIONID-consumer_1.0':
                    tokens["jsessionid"] = cookie['value']
                elif cookie['name'] == 'XSRF-TOKEN':
                    tokens["xsrf_token"] = cookie['value']
            
            logging.info(f"Captured Cookies: JSESSION={tokens['jsessionid']}, XSRF={tokens['xsrf_token']}")
            
            # Trigger a dummy request to capture the RPC hash by just filling the street box and hitting Enter
            # The API will complain but it still sends the payload with the RPC Hash
            await asyncio.sleep(1)
            street_input = page.locator("input.gwt-SuggestBox.form-control").first
            await street_input.fill("100 Main St", force=True, timeout=10000)
            await street_input.press("Enter")
            await street_input.press("Tab")
            await asyncio.sleep(1)
            
            try:
                go_button = page.locator("button.btn-primary:has-text('Go!')").first
                await go_button.click(force=True, timeout=5000)
            except:
                logging.error("Could not find Go button")
            
            # Wait for the network request to be captured
            await asyncio.sleep(4)
            
            # Validate and save
            if all(tokens.values()):
                with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                    json.dump(tokens, f)
                logging.info(f"Successfully saved tokens to {TOKEN_FILE}")
            else:
                logging.error(f"Failed to capture all tokens: {tokens}")
                
        except Exception as e:
            logging.error(f"Error scraping tokens: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_tokens())
