import json
from urllib.parse import urljoin, urlparse, parse_qs
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    playwright = sync_playwright().start()
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









