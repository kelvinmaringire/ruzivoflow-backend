import json
from datetime import datetime, timedelta
from asgiref.sync import sync_to_async
from urllib.parse import urljoin, urlparse, parse_qs
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

from .models import BetwayOdds
from .leagues import country_leagues


async def fetch_odds():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        )
        context.set_default_timeout(60000)
        page = await context.new_page()

        print("Opening new page")

        games = []

        # Iterate through countries and leagues
        for country, leagues in country_leagues.items():
            for league_name, league_id in leagues.items():
                print(league_name)
                print(league_id)
                # Construct the URL
                league_url = (
                    f"https://www.betway.co.za/Event/FilterEventsGet?"
                    f"sportConfigId=00000000-0000-0000-da7a-000000550001&"
                    f"feedDataTypeId=00000000-0000-0000-da7a-000000580001&"
                    f"leagueIds={league_id}&"
                    f"PredeterminedTime=Tomorrow"
                )
                # print(f"Scraping {league_name} ({country}) -> {league_url}")

                try:
                    # Navigate to the URL
                    await page.goto(league_url)
                    await page.wait_for_load_state('networkidle')
                except PlaywrightTimeoutError:
                    print(f"Timeout loading {league_url}, skipping...")
                    continue

                # Extract relative game URLs
                try:
                    relative_game_url_elements = await page.locator(
                        'div#fixturesToReplace div.eventRow div#eventDetails_0 > div.inplayStatusDetails.PaddingScreen > a'
                    ).all()
                except PlaywrightTimeoutError:
                    print(f"Error locating game URLs for league {league_name}, skipping...")
                    continue

                # Collect game URLs
                relative_game_urls = [await element.get_attribute('href') for element in relative_game_url_elements]
                # print(f"Found game URLs for {league_name}: {relative_game_urls}")
                today = datetime.today()
                tomorrow = today + timedelta(days=1)
                tomorrow_str = tomorrow.strftime("%Y%m%d")
                filtered_urls = [url for url in relative_game_urls if f"datefilter={tomorrow_str}" in url]  # unused
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
                    new_url = original_url.replace('eventId=026e4607-0000-0000-0000-000000000000',
                                                   f'eventId={event_id}')

                    #print('---- New Url-----')
                    #print(new_url)

                    try:
                        await page.goto(new_url)
                        await page.wait_for_load_state('networkidle')
                    except PlaywrightTimeoutError:
                        print(f"Error loading event details for {new_url}, skipping...")
                        continue

                    # Scrape match odds
                    match_result_1x2 = await page.locator(
                        "[data-translate-market='Match Result (1X2)']" "[data-translate-type='outcome']"
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

                    try:
                        home_target_element = page.locator(
                            '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{home_team}"]')
                        home_parent_locator = home_target_element.locator('xpath=..').locator('xpath=..')
                        home_element_with_new_line = await home_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        home_win = safe_float(home_element_with_new_line)
                    except PlaywrightTimeoutError:
                        home_win = None

                    try:
                        away_target_element = page.locator(
                            '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{away_team}"]')
                        away_parent_locator = away_target_element.locator('xpath=..').locator('xpath=..')
                        away_element_with_new_line = await away_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        away_win = safe_float(away_element_with_new_line)
                    except PlaywrightTimeoutError:
                        away_win = None

                    double_chances = await page.locator(
                        "[data-translate-market='Double Chance']" "[data-translate-key='Draw']").all()

                    if double_chances:
                        try:
                            home_draw_target_element = double_chances[0]
                            home_draw_parent_locator = home_draw_target_element.locator('xpath=..').locator('xpath=..')
                            home_draw_element_with_new_line = await home_draw_parent_locator.locator(
                                'div.outcome-pricedecimal').text_content()
                            home_draw = safe_float(home_draw_element_with_new_line)
                        except PlaywrightTimeoutError:
                            home_draw = None

                        try:
                            away_draw_target_element = double_chances[1]
                            away_draw_parent_locator = away_draw_target_element.locator('xpath=..').locator('xpath=..')
                            away_draw_element_with_new_line = await away_draw_parent_locator.locator(
                                'div.outcome-pricedecimal').text_content()
                            away_draw = safe_float(away_draw_element_with_new_line)
                        except PlaywrightTimeoutError:
                            away_draw = None
                    else:
                        home_draw = None
                        away_draw = None

                    try:
                        over15_target_element = page.locator(
                            "[data-translate-market='Overs/Unders (Total 1.5)']" "[data-translate-key='Over 1.5']")
                        over15_parent_locator = over15_target_element.locator('xpath=..').locator('xpath=..')
                        over15_element_with_new_line = await over15_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        over15 = safe_float(over15_element_with_new_line)
                    except PlaywrightTimeoutError:
                        over15 = None

                    try:
                        under35_target_element = page.locator(
                            "[data-translate-market='Overs/Unders (Total 3.5)']" "[data-translate-key='Under 3.5']")
                        under35_parent_locator = under35_target_element.locator('xpath=..').locator('xpath=..')
                        under35_element_with_new_line = await under35_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        under35 = safe_float(under35_element_with_new_line)
                    except PlaywrightTimeoutError:
                        under35 = None

                    try:
                        bttsy_target_element = page.locator(
                            "[data-translate-market='Both Teams To Score']" "[data-translate-key='Yes']")
                        bttsy_parent_locator = bttsy_target_element.locator('xpath=..').locator('xpath=..')
                        bttsy_element_with_new_line = await bttsy_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        bttsy = safe_float(bttsy_element_with_new_line)
                    except PlaywrightTimeoutError:
                        bttsy = None

                    try:
                        bttsn_target_element = page.locator(
                            "[data-translate-market='Both Teams To Score']" "[data-translate-key='No']")
                        bttsn_parent_locator = bttsn_target_element.locator('xpath=..').locator('xpath=..')
                        bttsn_element_with_new_line = await bttsn_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        bttsn = safe_float(bttsn_element_with_new_line)
                    except PlaywrightTimeoutError:
                        bttsn = None

                    try:
                        home05_target_element = page.locator(
                            f'[data-translate-market="{home_team} Total (Total 0.5)"]' '[data-translate-key="Over 0.5"]')
                        home05_parent_locator = home05_target_element.locator('xpath=..').locator('xpath=..')
                        home05_element_with_new_line = await home05_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
                        home05 = safe_float(home05_element_with_new_line)
                    except PlaywrightTimeoutError:
                        home05 = None

                    try:
                        away05_target_element = page.locator(
                            f'[data-translate-market="{away_team} Total (Total 0.5)"]' '[data-translate-key="Over 0.5"]')
                        away05_parent_locator = away05_target_element.locator('xpath=..').locator('xpath=..')
                        away05_element_with_new_line = await away05_parent_locator.locator(
                            'div.outcome-pricedecimal').text_content()
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


# https://www.betway.co.za/Event/FilterEventsGet?sportConfigId=00000000-0000-0000-da7a-000000550001&feedDataTypeId=00000000-0000-0000-da7a-000000580001&leagueIds=a0fef402-d616-e811-80cd-00155d4cf19b&PredeterminedTime=Tomorrow
# https://www.betway.co.za/Event/FilterEventsGet?sportConfigId=00000000-0000-0000-da7a-000000550001&feedDataTypeId=00000000-0000-0000-da7a-000000580001&leagueIds=5546c4d7-d816-e811-80cd-00155d4cf19b,69721e2f-d816-e811-80cd-00155d4cf19b,8e239cd3-d716-e811-80cd-00155d4cf19b,d7c74297-d616-e811-80cd-00155d4cf19b,15230075-d616-e811-80cd-00155d4cf19b,2ead1689-d816-e811-80cd-00155d4cf19b&PredeterminedTime=Tomorrow
