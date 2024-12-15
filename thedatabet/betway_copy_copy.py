  import json
from datetime import datetime, timedelta
from asgiref.sync import sync_to_async
from urllib.parse import urljoin, urlparse, parse_qs
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

from .models import BetwayOdds


async def fetch_odds():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        )
        context.set_default_timeout(600000)
        page = await context.new_page()

        print("Opening new page")

        games = []
        country_leagues = {
            'England': {
                'Premier League': '5546c4d7-d816-e811-80cd-00155d4cf19b',
                'EFL Cup': '69721e2f-d816-e811-80cd-00155d4cf19b'

            },
            'Spain': {
                'La liga': 'c97c77e3-d516-e811-80cd-00155d4cf19b',
                'Super Cup': ',f2913121-f887-e811-80d5-00155d4a2d29'
            }
        }

        #https://www.betway.co.za/Event/FilterEventsGet?sportConfigId=00000000-0000-0000-da7a-000000550001&feedDataTypeId=00000000-0000-0000-da7a-000000580001&leagueIds=a0fef402-d616-e811-80cd-00155d4cf19b&PredeterminedTime=Tomorrow
        #https://www.betway.co.za/Event/FilterEventsGet?sportConfigId=00000000-0000-0000-da7a-000000550001&feedDataTypeId=00000000-0000-0000-da7a-000000580001&leagueIds=5546c4d7-d816-e811-80cd-00155d4cf19b,69721e2f-d816-e811-80cd-00155d4cf19b,8e239cd3-d716-e811-80cd-00155d4cf19b,d7c74297-d616-e811-80cd-00155d4cf19b,15230075-d616-e811-80cd-00155d4cf19b,2ead1689-d816-e811-80cd-00155d4cf19b&PredeterminedTime=Tomorrow
        countries = ['esp', 'sco', 'eng']
        countries1 = [
            'eng', 'esp', 'ger', 'ita', 'fra', 'rsa', 'por', 'netherlands', 'usa', 'dza', 'alb', 'arg', 'aut', 'aut_am',
            'aze', 'bel', 'bol', 'bra', 'bgr', 'canada', 'challenger', 'chi', 'chn', 'clubs', 'col', 'cro', 'cze', 'den',
            'denmark_amateur', 'ecu', 'egy', 'est', 'ethiopia', 'faroe_islands', 'fin', 'geo', 'ger_am', 'gre', 'ice',
            'int', 'ireland', 'civ', 'jpn', 'kazakhstan', 'kaz', 'lat', 'lith', 'mas', 'mex', 'mne', 'nzl', 'nir', 'nor',
            'par', 'per', 'phi', 'pol', 'republic_of_korea', 'rou', 'sco', 'sen', 'singapore', 'slv', 'spain_amateur', 'swe',
            'challenger', 'sui', 'trinidad_and_tobago', 'tun', 'tur_am', 'uae', 'ukr', 'ury', 'uzb', 'vnm', 'zambia'
        ]

        for country in countries:
            country_url = f'https://www.betway.co.za/sport/soccer/{country}/'
            try:
                await page.goto(country_url)
                await page.wait_for_load_state('networkidle')
            except PlaywrightTimeoutError:
                print(f"Timeout loading {country_url}, skipping...")
                continue

            try:
                relative_game_url_elements = await page.locator(
                    'div#fixturesToReplace div.eventRow div#eventDetails_0 > div.inplayStatusDetails.PaddingScreen > a'
                ).all()
            except PlaywrightTimeoutError:
                print(f"Error locating game URLs for country {country}, skipping...")
                continue

            relative_game_urls = [await element.get_attribute('href') for element in relative_game_url_elements]
            print(relative_game_urls)
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
                new_url = f'https://www.betway.co.za/Bet/EventMultiMarket?eventId={event_id}&isPopular=false&pageNum=1&isFullView=false&loadAll=true'

                try:
                    await page.goto(new_url)
                    await page.wait_for_load_state('networkidle')
                except PlaywrightTimeoutError:
                    print(f"Error loading event details for {new_url}, skipping...")
                    continue

                # Scrape match odds
                match_result_1x2 = await page.locator(
                    "[data-translate-market='Match Result (1X2)'] [data-translate-type='outcome']"
                ).all_text_contents()
                if len(match_result_1x2) >= 3:
                    home_team = match_result_1x2[0].strip()
                    away_team = match_result_1x2[2].strip()
                else:
                    print(f"Could not retrieve match result for country {country}, skipping...")
                    continue  # Skip this game

                def safe_float(value):
                    try:
                        return float(value.strip()) if value.strip() else None
                    except ValueError:
                        return None

                # Helper function to extract odds safely
                async def extract_odds(selector, key=None):
                    try:
                        target_element = page.locator(selector)
                        if key:
                            target_element = target_element.locator(f"[data-translate-key='{key}']")
                        parent_locator = target_element.locator('xpath=..').locator('xpath=..')
                        value = await parent_locator.locator('div.outcome-pricedecimal').text_content()
                        return safe_float(value)
                    except PlaywrightTimeoutError:
                        return None

                home_win = await extract_odds("[data-translate-market='Match Result (1X2)']", home_team)
                away_win = await extract_odds("[data-translate-market='Match Result (1X2)']", away_team)
                over15 = await extract_odds("[data-translate-market='Overs/Unders (Total 1.5)']", "Over 1.5")
                under35 = await extract_odds("[data-translate-market='Overs/Unders (Total 3.5)']", "Under 3.5")
                bttsy = await extract_odds("[data-translate-market='Both Teams To Score']", "Yes")
                bttsn = await extract_odds("[data-translate-market='Both Teams To Score']", "No")
                home05 = await extract_odds(f"[data-translate-market='{home_team} Total (Total 0.5)']", "Over 0.5")
                away05 = await extract_odds(f"[data-translate-market='{away_team} Total (Total 0.5)']", "Over 0.5")

                game = {
                    'home_team': home_team,
                    'away_team': away_team,
                    'country': country,
                    'league': capitalized_league,
                    'home_win': home_win,
                    'away_win': away_win,
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

        await browser.close()
        print("Games fetched successfully.")
        return games


async def save_odds(games):
    today = datetime.now()
    tomo = today + timedelta(days=1)
    with open('games.json', 'w') as f:
        json.dump(games, f, indent=4)
    betway_odds = BetwayOdds(
        date=tomo,
        odds=games
    )
    await sync_to_async(betway_odds.save)()


async def main():
    print("Starting main coroutine...")
    games = await fetch_odds()
    await save_odds(games)
    print("Finished main coroutine.")


if __name__ == '__main__':
    import asyncio
    print("Starting script execution...")
    asyncio.run(main())
    print("Script execution finished.")