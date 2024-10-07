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
        url = "https://1xbet.com/en/line/football"
        await page.goto(url)
        liga_menu = await page.locator(".liga_menu").all()
        subcategory_menu = await page.locator(".subcategory-menu").all()
        print(len(liga_menu))

        for item in liga_menu:
            await item.click()
        print(len(subcategory_menu))

        await browser.close()



"""
def main():
    playwright = async_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.set_default_timeout(timeout=60000)
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    url = "https://1xbet.com/en/line/football"
    page.goto(url)
    page.wait_for_load_state('networkidle')
    tournaments = page.locator(".liga_menu").all()
    for tournament in tournaments:
        tournament.click()
        game_listitems = tournament.locator("ul.event_menu").filter(has_text="11/06/2024").all()
        for game_url in game_listitems:
            pass

"""







