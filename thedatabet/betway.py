import json
import datetime
from asgiref.sync import sync_to_async, async_to_sync
from urllib.parse import urljoin, urlparse, parse_qs
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

from .models import BetwayOdds

def fetch_odds():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    )
    context.set_default_timeout(timeout=60000)
    page = context.new_page()

    print("Opening new page ")

    games = []
    countries1 = ['usa', 'aut', 'bel', 'den']

    countries = [
        'eng', 'esp', 'ger', 'ita', 'fra', 'rsa', 'por', 'netherlands', 'usa', 'dza', 'arg', 'aut', 'aut_am',
        'aze', 'bel', 'bol', 'bra', 'bgr', 'canada', 'challenger', 'chi', 'chn', 'clubs', 'col', 'cro', 'cze', 'den',
        'denmark_amateur', 'ecu', 'egy', 'est', 'ethiopia', 'faroe_islands', 'fin', 'geo', 'ger_am', 'gre', 'ice',
        'int', 'ireland', 'civ', 'jpn', 'kazakhstan', 'kaz', 'lat', 'lith', 'mas', 'mex', 'mne', 'nzl', 'nir', 'nor',
        'par', 'per', 'phi', 'pol', 'republic_of_korea', 'rou', 'sco', 'sen', 'singapore', 'slv', 'spain_amateur', 'swe',
        'challenger', 'sui', 'trinidad_and_tobago', 'tun', 'tur_am', 'uae', 'ukr', 'ury', 'uzb', 'vnm', 'zambia'
    ]
    for country in countries:
        country_url = f'https://www.betway.co.za/sport/soccer/{country}/'
        try:
            page.goto(country_url)
            page.wait_for_load_state('networkidle')
        except PlaywrightTimeoutError:
            continue

        try:
            relative_game_url_elements = page.locator(
                'div#fixturesToReplace div.eventRow div#eventDetails_0 > div.inplayStatusDetails.PaddingScreen > a').all()
        except PlaywrightTimeoutError:
            continue

        relative_game_urls = [url.get_attribute('href') for url in relative_game_url_elements]
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        tomorrow_str = tomorrow.strftime("%Y%m%d")
        filtered_urls = [url for url in relative_game_urls if f"datefilter={tomorrow_str}" in url]
        base_url = 'https://www.betway.co.za/'

        for relative_game_url in filtered_urls:
            absolute_url = urljoin(base_url, relative_game_url)
            parsed_url = urlparse(absolute_url)
            path_components = parsed_url.path.split('/')
            country_code = path_components[3]
            league = path_components[4]
            league_without_underscores = league.replace("_", " ")
            capitalized_league = league_without_underscores.capitalize()
            query_params = parse_qs(parsed_url.query)
            date_time = query_params.get('datefilter', [''])[0]
            event_id = query_params.get('eventId', [''])[0]
            date = date_time[:8]
            time = date_time[8:]
            original_url = 'https://www.betway.co.za/Bet/EventMultiMarket?' \
                           'eventId=026e4607-0000-0000-0000-000000000000&' \
                           'FeedDataTypeId=00000000-0000-0000-0000-000000000000&' \
                           'isPopular=false&pageNum=1&isFullView=false&loadAll=true'
            new_url = original_url.replace('eventId=026e4607-0000-0000-0000-000000000000', f'eventId={event_id}')

            print('---- New Url-----')
            print(new_url)

            page.goto(new_url)
            page.wait_for_load_state('networkidle')
            match_result_1x2 = page.locator(
                "[data-translate-market='Match Result (1X2)']" "[data-translate-type='outcome']").all_text_contents()
            home_team = match_result_1x2[0].strip()
            away_team = match_result_1x2[2].strip()

            def safe_float(value):
                try:
                    return float(value.strip()) if value.strip() else None
                except ValueError:
                    return None

            try:
                home_target_element = page.locator(
                    '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{home_team}"]')
                home_parent_locator = home_target_element.locator('xpath=..').locator('xpath=..')
                home_element_with_new_line = home_parent_locator.locator('div.outcome-pricedecimal').text_content()
                home_win = safe_float(home_element_with_new_line)
            except PlaywrightTimeoutError:
                home_win = None

            try:
                away_target_element = page.locator(
                    '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{away_team}"]')
                away_parent_locator = away_target_element.locator('xpath=..').locator('xpath=..')
                away_element_with_new_line = away_parent_locator.locator('div.outcome-pricedecimal').text_content()
                away_win = safe_float(away_element_with_new_line)
            except PlaywrightTimeoutError:
                away_win = None

            double_chances = page.locator("[data-translate-market='Double Chance']" "[data-translate-key='Draw']").all()

            if double_chances:
                try:
                    home_draw_target_element = double_chances[0]
                    home_draw_parent_locator = home_draw_target_element.locator('xpath=..').locator('xpath=..')
                    home_draw_element_with_new_line = home_draw_parent_locator.locator(
                        'div.outcome-pricedecimal').text_content()
                    home_draw = safe_float(home_draw_element_with_new_line)
                except PlaywrightTimeoutError:
                    home_draw = None

                try:
                    away_draw_target_element = double_chances[1]
                    away_draw_parent_locator = away_draw_target_element.locator('xpath=..').locator('xpath=..')
                    away_draw_element_with_new_line = away_draw_parent_locator.locator(
                        'div.outcome-pricedecimal').text_content()
                    away_draw = safe_float(away_draw_element_with_new_line)
                except PlaywrightTimeoutError:
                    away_draw = None
            else:
                home_draw = None
                away_draw = None

            try:
                over15_target_element = page.locator(
                    "[data-translate-market='Overs/Unders']" "[data-translate-key='Over 1.5']")
                over15_parent_locator = over15_target_element.locator('xpath=..').locator('xpath=..')
                over15_element_with_new_line = over15_parent_locator.locator('div.outcome-pricedecimal').text_content()
                over15 = safe_float(over15_element_with_new_line)
            except PlaywrightTimeoutError:
                over15 = None

            try:
                under35_target_element = page.locator(
                    "[data-translate-market='Overs/Unders']" "[data-translate-key='Under 3.5']")
                under35_parent_locator = under35_target_element.locator('xpath=..').locator('xpath=..')
                under35_element_with_new_line = under35_parent_locator.locator(
                    'div.outcome-pricedecimal').text_content()
                under35 = safe_float(under35_element_with_new_line)
            except PlaywrightTimeoutError:
                under35 = None

            try:
                bttsy_target_element = page.locator(
                    "[data-translate-market='Both Teams To Score']" "[data-translate-key='Yes']")
                bttsy_parent_locator = bttsy_target_element.locator('xpath=..').locator('xpath=..')
                bttsy_element_with_new_line = bttsy_parent_locator.locator('div.outcome-pricedecimal').text_content()
                bttsy = safe_float(bttsy_element_with_new_line)
            except PlaywrightTimeoutError:
                bttsy = None

            try:
                bttsn_target_element = page.locator(
                    "[data-translate-market='Both Teams To Score']" "[data-translate-key='No']")
                bttsn_parent_locator = bttsn_target_element.locator('xpath=..').locator('xpath=..')
                bttsn_element_with_new_line = bttsn_parent_locator.locator('div.outcome-pricedecimal').text_content()
                bttsn = safe_float(bttsn_element_with_new_line)
            except PlaywrightTimeoutError:
                bttsn = None

            try:
                home05_target_element = page.locator(
                     f'[data-translate-market="{home_team} Total"]' '[data-translate-key="Over 0.5"]')
                home05_parent_locator = home05_target_element.locator('xpath=..').locator('xpath=..')
                home05_element_with_new_line = home05_parent_locator.locator('div.outcome-pricedecimal').text_content()
                home05 = safe_float(home05_element_with_new_line)
            except PlaywrightTimeoutError:
                home05 = None

            try:
                away05_target_element = page.locator(
                    f'[data-translate-market="{away_team} Total"]' '[data-translate-key="Over 0.5"]')
                away05_parent_locator = away05_target_element.locator('xpath=..').locator('xpath=..')
                away05_element_with_new_line = away05_parent_locator.locator('div.outcome-pricedecimal').text_content()
                away05 = safe_float(away05_element_with_new_line)
            except PlaywrightTimeoutError:
                away05 = None

            game = {
                'home_team': home_team,
                'away_team': away_team,
                'country': country,
                'league': capitalized_league,
                'home_win': home_win,
                'away_win': away_win,
                'home_draw': home_draw,
                'away_draw': away_draw,
                'over15': over15,
                'under35': under35,
                'bttsy': bttsy,
                'bttsn': bttsn,
                'home05': home05,
                'away05': away05,
                'date': date,
                'time': time
            }
            games.append(game)

    browser.close()
    playwright.stop()

    print("Games fetched successfully.")

    return games

async def save_odds(games):
    today = datetime.now()
    tomo = today + timedelta(days=1)
    #games_json = json.dumps(games)
    with open('games.json', 'w') as f:
        json.dump(games, f, indent=4)
    betway_odds = BetwayOdds(
        date=tomo,
        odds=games
    )
    await sync_to_async(betway_odds.save)()

def main():
    games = fetch_odds()
    async_to_sync(save_odds)(games)

if __name__ == '__main__':
    main()
