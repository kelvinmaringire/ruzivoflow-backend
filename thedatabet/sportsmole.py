import json
from urllib.parse import urljoin, urlparse, parse_qs
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.set_default_timeout(timeout=90000)
    page = context.new_page()
    url = "https://1xbet.com/en/line/football"
    page.goto(url)
    page.wait_for_load_state('networkidle')
    page.locator('li.top-menu-list__item.menu_button.tutorial.to_bottom_left').click()
    page.locator('#line_href').click()






