from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def main():
    async with async_playwright() as playwright:
        #playwright = await async_playwright().start()
        # Your async code goes here
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        context.set_default_timeout(timeout=60000)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        url = "https://1xbet.com/en/line/football/118587-uefa-champions-league/239514862-benfica-barcelona"
        await page.goto(url)
        await page.wait_for_selector('#allBetsTable .markets-canvas canvas')
        # Screenshot the canvas
        await page.screenshot(path="canvas.png", full_page=True, timeout=120000, omit_background=False, animations="disabled")

        # (Optional) Use JavaScript to inspect the canvas
        script = """
        const canvas = document.querySelector('#allBetsTable .markets-canvas canvas');
        const context = canvas.getContext('2d');
        return canvas.toDataURL();
        """
        canvas_data_url = page.evaluate(script)
        print(canvas_data_url)
        await browser.close()
        """
        url = "https://1xbet.com/en/line/football"
        await page.goto(url)
        liga_menu = await page.locator(".liga_menu").all()
        subcategory_menu = await page.locator(".subcategory-menu").all()
        print(len(liga_menu))

        for item in liga_menu:
            await item.click()
        print(len(subcategory_menu))
        
        """

        #await browser.close()











