from playwright.async_api import async_playwright
from io import BytesIO
import asyncio

async def capture_bubblemap(chain: str, contract_address: str) -> BytesIO:
    """Capture bubble map screenshot using Playwright."""
    url = f"https://app.bubblemaps.io/{chain}/token/{contract_address}?small_text&hide_context"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 800, "height": 600})
        
        try:
            await page.goto(url, timeout=15000, wait_until="networkidle")
            await page.wait_for_selector(".bubble-map-container", timeout=10000)
            
            screenshot = await page.screenshot(type="png")
            return BytesIO(screenshot)
        except Exception as e:
            print(f"Screenshot error: {e}")
            return None
        finally:
            await browser.close()