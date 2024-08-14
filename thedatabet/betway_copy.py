import json
import datetime
from asgiref.sync import sync_to_async
from urllib.parse import urljoin, urlparse, parse_qs
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

from .models import BetwayOdds


def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.set_default_timeout(timeout=60000)
    page = context.new_page()


    print("Opening new page ")

    games = []
    countries = [
        'eng', 'esp', 'ger', 'ita', 'fra', 'rsa', 'por', 'netherlands', 'usa', 'dza', 'arg', 'aut', 'aut_am',
        'aze', 'bel', 'bol', 'bra', 'bgr', 'canada', 'challenger', 'chi', 'chn', 'clubs', 'col', 'cro', 'cze', 'den',
        'denmark_amateur', 'ecu', 'egy', 'est', 'ethiopia', 'faroe_islands', 'fin', 'geo', 'ger_am', 'gre', 'ice',
        'int', 'ireland', 'civ', 'jpn', 'kazakhstan', 'kaz', 'lat', 'lith', 'mas', 'mex', 'mne', 'nzl', 'nir', 'nor',
        'par', 'per', 'phi', 'pol', 'republic_of_korea', 'rou', 'sco', 'sen', 'singapore', 'spain_amateur', 'swe',
        'challenger', 'sui', 'trinidad_and_tobago', 'tun', 'tur_am', 'uae', 'ukr', 'ury', 'uzb', 'vnm', 'zambia'
    ]
    countries1 = [
         'swe',
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
            relative_game_url_elements = page.locator('div#fixturesToReplace div.eventRow div#eventDetails_0 > div.inplayStatusDetails.PaddingScreen > a').all()
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
            # Extract the path components
            path_components = parsed_url.path.split('/')
            country_code = path_components[3]
            league = path_components[4]
            # Remove underscores
            league_without_underscores = league.replace("_", " ")
            # Capitalize the string
            capitalized_league = league_without_underscores.capitalize()

            # Extract the query parameters
            query_params = parse_qs(parsed_url.query)
            date_time = query_params.get('datefilter', [''])[0]
            event_id = query_params.get('eventId', [''])[0]

            # Extract the date and time from the date_time string
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

            # Home Win
            try:
                home_target_element = page.locator(
                    '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{home_team}"]')
                home_parent_locator = home_target_element.locator('xpath=..').locator('xpath=..')
                home_element_with_new_line = home_parent_locator.locator('div.outcome-pricedecimal').text_content()
                home_win = float(home_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                home_win = None

            # Away Win
            try:
                away_target_element = page.locator(
                    '[data-translate-market="Match Result (1X2)"]' f'[data-translate-key="{away_team}"]')
                away_parent_locator = away_target_element.locator('xpath=..').locator('xpath=..')
                away_element_with_new_line = away_parent_locator.locator('div.outcome-pricedecimal').text_content()
                away_win = float(away_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                away_win = None

            double_chances = page.locator("[data-translate-market='Double Chance']" "[data-translate-key='Draw']").all()

            if double_chances:

                # Home or Draw
                try:
                    home_draw_target_element = double_chances[0]
                    home_draw_parent_locator = home_draw_target_element.locator('xpath=..').locator('xpath=..')
                    home_draw_element_with_new_line = home_draw_parent_locator.locator(
                        'div.outcome-pricedecimal').text_content()
                    home_draw = float(home_draw_element_with_new_line.strip())
                except PlaywrightTimeoutError:
                    home_draw = None


                try:
                    # Away or Draw
                    away_draw_target_element = double_chances[1]
                    away_draw_parent_locator = away_draw_target_element.locator('xpath=..').locator('xpath=..')
                    away_draw_element_with_new_line = away_draw_parent_locator.locator(
                        'div.outcome-pricedecimal').text_content()
                    away_draw = float(away_draw_element_with_new_line.strip())
                except PlaywrightTimeoutError:
                    away_draw = None

            else:
                home_draw = None
                away_draw = None

            # Over 1.5
            try:
                over15_target_element = page.locator(
                    "[data-translate-market='Overs/Unders']" "[data-translate-key='Over 1.5']")
                over15_parent_locator = over15_target_element.locator('xpath=..').locator('xpath=..')
                over15_element_with_new_line = over15_parent_locator.locator('div.outcome-pricedecimal').text_content()
                over15 = float(over15_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                over15 = None

            # Under 3.5
            try:
                under35_target_element = page.locator(
                    "[data-translate-market='Overs/Unders']" "[data-translate-key='Under 3.5']")
                under35_parent_locator = under35_target_element.locator('xpath=..').locator('xpath=..')
                under35_element_with_new_line = under35_parent_locator.locator(
                    'div.outcome-pricedecimal').text_content()
                under35 = float(under35_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                under35 = None

            # BTTS Yes
            try:
                bttsy_target_element = page.locator(
                    "[data-translate-market='Both Teams To Score']" "[data-translate-key='Yes']")
                bttsy_parent_locator = bttsy_target_element.locator('xpath=..').locator('xpath=..')
                bttsy_element_with_new_line = bttsy_parent_locator.locator('div.outcome-pricedecimal').text_content()
                bttsy = float(bttsy_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                bttsy = None

            # BTTS No
            try:
                bttsn_target_element = page.locator(
                    "[data-translate-market='Both Teams To Score']" "[data-translate-key='No']")
                bttsn_parent_locator = bttsn_target_element.locator('xpath=..').locator('xpath=..')
                bttsn_element_with_new_line = bttsn_parent_locator.locator('div.outcome-pricedecimal').text_content()
                bttsn = float(bttsn_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                bttsn = None


            # Home Over 0.5
            try:
                home05_target_element = page.locator(
                    f'[data-translate-market="{home_team} Total"]' '[data-translate-key="Over 0.5"]')
                home05_parent_locator = home05_target_element.locator('xpath=..').locator('xpath=..')
                home05_element_with_new_line = home05_parent_locator.locator('div.outcome-pricedecimal').text_content()
                home05 = float(home05_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                home05 = None

            # Away Over 0.5
            try:
                away05_target_element = page.locator(
                    f'[data-translate-market="{away_team} Total"]' '[data-translate-key="Over 0.5"]')
                away05_parent_locator = away05_target_element.locator('xpath=..').locator('xpath=..')
                away05_element_with_new_line = away05_parent_locator.locator('div.outcome-pricedecimal').text_content()
                away05 = float(away05_element_with_new_line.strip())
            except PlaywrightTimeoutError:
                away05 = None

            games.append({
                'country_code': country_code,
                'league': capitalized_league,
                'date': date,
                'time': time,
                'home_team': home_team,
                'away_team': away_team,
                'home_win': home_win,
                'away_win': away_win,
                'home_draw': home_draw,
                'away_draw': away_draw,
                'home05': home05,
                'away05': away05,
                'over_15': over15,
                'under_35': under35,
                'btts_yes': bttsy,
                'btts_no': bttsn,
            })
    with open('games.json', 'w') as f:
        json.dump(games, f, indent=4)
    today = datetime.now()
    tomo = today + timedelta(days=1)
    games_json = json.dumps(games)
    await sync_to_async(BetwayOdds.objects.create)(
        date=tomo,
        odds=games_json
    )
    print("Closing Browser")
    browser.close()
    print("Stopping Playwright")
    playwright.stop()




    new_games_df["home_win"] = np.where(
        (new_games_df['Predicted_Host_SC'] > new_games_df['Predicted_Guest_SC']) &
         (new_games_df['Predicted_result'] < 1.5) &
         (new_games_df['Host_Perfom'] < new_games_df['Guest_Concede']),
         1, 0)

    new_games_df["away_win"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + 1.5) < new_games_df['Predicted_Guest_SC']) &
        (new_games_df['Predicted_result'] > 2.5) &
        (new_games_df['Guest_Perfom'] < new_games_df['Host_Concede']),
        1, 0)

    new_games_df["over_25"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + new_games_df['Predicted_Guest_SC']) > 3) &
        (new_games_df['goalsavg'] > 3) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] + new_games_df['Guest_Perfom'] + new_games_df[
            'Guest_Concede']) > 5.8),
        1, 0)

    new_games_df["under_25"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + new_games_df['Predicted_Guest_SC']) < 1.5) &
        (new_games_df['goalsavg'] < 1.5) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] +
          new_games_df['Guest_Perfom'] + new_games_df['Guest_Concede']) < 4.5),
        1, 0
    )

    new_games_df["btts"] = np.where(
        (new_games_df['Predicted_Host_SC'] > 1.75) & (new_games_df['Predicted_Guest_SC'] > 1.75) &
        (new_games_df['goalsavg'] > 3) &
        (new_games_df['Predicted_result'] >= 1.75) & (new_games_df['Predicted_result'] <= 2.25) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] + new_games_df['Guest_Perfom'] + new_games_df[
            'Guest_Concede']) > 6),
        1, 0
    )

    new_games_df["home_over_15"] = np.where(
        (new_games_df['Predicted_Host_SC'] > 2) &
        (new_games_df['Predicted_result'] < 1.5) &
        (new_games_df['Host_Perfom'] > 1.5) &
        (new_games_df['Guest_Concede'] > 1.5),
        1, 0
    )

    new_games_df["away_over_15"] = np.where(
        (new_games_df['Predicted_Guest_SC'] > 2) &
        (new_games_df['Predicted_result'] > 2.5) &
        (new_games_df['Guest_Perfom'] > 1.5) &
        (new_games_df['Host_Concede'] > 1.5),
        1, 0
    )

    new_games_df["home_draw"] = np.where(
        ((new_games_df['Pred_1'] + new_games_df['Pred_X']) > 75) &
        (new_games_df['Predicted_Host_SC'] > (new_games_df['Predicted_Guest_SC'] + 0.5)) &
         (new_games_df['Predicted_result'] < 1.5) &
         (new_games_df['Host_Perfom'] < new_games_df['Guest_Concede']),
         1, 0
         )

    new_games_df["away_draw"] = np.where(
        (new_games_df['Pred_2'] + new_games_df['Pred_X'] > 75) &
        ((new_games_df['Predicted_Host_SC'] + 0.5) < new_games_df['Predicted_Guest_SC']) &
        (new_games_df['Predicted_result'] > 2.5) &
        (new_games_df['Guest_Perfom'] < new_games_df['Host_Concede']),
        1, 0
    )