import json
import os

import numpy as np
import pandas as pd
from unidecode import unidecode
from datetime import datetime, timedelta

from django.conf import settings
from .models import BettingTips, BettingStats


def main():


    today_date = datetime.now()
    yesterday_date = today_date - timedelta(days=1)

    print("Getting data from database")
    yesterday_data = BettingTips.objects.get(date=yesterday_date)
    file_games_df = pd.DataFrame(yesterday_data.games)
    columns_to_drop = ["Host_SC", "Guest_SC"]
    file_games_df.drop(columns=columns_to_drop, inplace=True)
    filter_date = yesterday_date.strftime('%Y-%m-%d')

    file_path = os.path.join(settings.MEDIA_ROOT, 'documents/forebet_data.json')

    print("Getting data from file")
    # Load data from JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Iterate through the list to find the dictionary with the specified date
    filtered_data = None
    for item in data:
        if filter_date in item:
            filtered_data = item[filter_date]
            break


    print("Create Dataframe from file")
    new_games = filtered_data[0]
    new_games_df = pd.DataFrame(new_games,
                                columns=["DATE_BAH", "league_id", "Pred_1", "Pred_X", "Pred_2", "host_id", "guest_id",
                                         "HOST_NAME", "GUEST_NAME", "Host_SC", "Guest_SC", "host_sc_pr", "guest_sc_pr",
                                         "goalsavg"])
    new_games_df.dropna(inplace=True)
    new_games_df["DATE_BAH"] = new_games_df["DATE_BAH"].astype("datetime64[ns]")
    new_games_df["DATE_BAH"] = new_games_df["DATE_BAH"].dt.strftime('%m/%d %H:%M')
    new_games_df["league_id"] = new_games_df["league_id"].astype("int16")
    new_games_df["host_id"] = new_games_df["host_id"].astype("int16")
    new_games_df["guest_id"] = new_games_df["guest_id"].astype("int16")
    new_games_df["Pred_1"] = new_games_df["Pred_1"].astype("int16")
    new_games_df["Pred_X"] = new_games_df["Pred_X"].astype("int16")
    new_games_df["Pred_2"] = new_games_df["Pred_2"].astype("int16")
    new_games_df["goalsavg"] = new_games_df["goalsavg"].astype("float16")
    new_games_df["host_sc_pr"] = new_games_df["host_sc_pr"].astype("int16")
    new_games_df["guest_sc_pr"] = new_games_df["guest_sc_pr"].astype("int16")
    new_games_df["Host_SC"] = new_games_df["Host_SC"].astype("int16")
    new_games_df["Guest_SC"] = new_games_df["Guest_SC"].astype("int16")

    # Replace special characters in specific columns
    new_games_df['HOST_NAME'] = new_games_df['HOST_NAME'].apply(lambda x: unidecode(x))
    new_games_df['GUEST_NAME'] = new_games_df['GUEST_NAME'].apply(lambda x: unidecode(x))

    print("Merging two databases")
    merged_df = pd.merge(file_games_df, new_games_df,
                         on=['league_id', 'Pred_1', 'Pred_X', 'Pred_2', 'host_id', 'guest_id', 'HOST_NAME',
                             'GUEST_NAME', 'host_sc_pr', 'guest_sc_pr', 'goalsavg'], how='left')
    merged_df.dropna(inplace=True)


    home_win = merged_df[merged_df['Host_SC'] > merged_df['Guest_SC']]
    away_win = merged_df[merged_df['Host_SC'] < merged_df['Guest_SC']]
    draw = merged_df[merged_df['Host_SC'] == merged_df['Guest_SC']]
    over_25 = merged_df[merged_df['Host_SC'] + merged_df['Guest_SC'] > 2.5]
    under_25 = merged_df[merged_df['Host_SC'] + merged_df['Guest_SC'] < 2.5]
    btts = merged_df[(merged_df['Host_SC'] > 1.5) & (merged_df['Guest_SC'] > 1.5)]
    home_over_15 = merged_df[merged_df['Host_SC'] > 1.5]
    away_over_15 = merged_df[merged_df['Guest_SC'] > 1.5]
    home_draw = merged_df[
        (merged_df['Host_SC'] > merged_df['Guest_SC']) | (merged_df['Host_SC'] == merged_df['Guest_SC'])]
    away_draw = merged_df[
        (merged_df['Host_SC'] < merged_df['Guest_SC']) | (merged_df['Host_SC'] == merged_df['Guest_SC'])]


    print("Calculating stats")

    average = {
        "home_win": home_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "away_win": away_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "draw": draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "over_25": over_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "under_25": under_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "btts": btts[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "home_over_15": home_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "away_over_15": away_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "home_draw": home_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
        "away_draw": away_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].mean().to_dict(),
    }
    describe = {
        "home_win": home_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "away_win": away_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "draw": draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "over_25": over_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "under_25": under_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "btts": btts[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "home_over_15": home_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "away_over_15": away_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "home_draw": home_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "away_draw": away_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
    }
    variance = {
        "home_win": home_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "away_win": away_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "draw": draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "over_25": over_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "under_25": under_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "btts": btts[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "home_over_15": home_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "away_over_15": away_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "home_draw": home_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
        "away_draw": away_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].var().to_dict(),
    }
    standard_deviation = {
        "home_win": home_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "away_win": away_win[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "draw": draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "over_25": over_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "under_25": under_25[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "btts": btts[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].describe().to_dict(),
        "home_over_15": home_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "away_over_15": away_over_15[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "home_draw": home_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
        "away_draw": away_draw[
            ["Predicted_result", "Pred_1", "Pred_X", "Pred_2", "host_sc_pr", "guest_sc_pr", "goalsavg", "Host_Perfom",
             "Host_Concede", "Guest_Perfom", "Guest_Concede", "Predicted_Host_SC", "Predicted_Guest_SC", "Host_SC",
             "Guest_SC"]].std().to_dict(),
    }

    print("Percentages & Lengths")

    home_win_df = merged_df[merged_df['home_win'] == 1]
    home_win_len = len(home_win_df)
    if not home_win_df.empty:
        home_win_percentage = round(
            (home_win_df[home_win_df['Host_SC'] > home_win_df['Guest_SC']].shape[0] / home_win_df.shape[0]) * 100, 2)
    else:
        home_win_percentage = 0

    away_win_df = merged_df[merged_df['away_win'] == 1]
    away_win_len = len(away_win_df)
    if not away_win_df.empty:
        away_win_percentage = round(
            (away_win_df[away_win_df['Host_SC'] < away_win_df['Guest_SC']].shape[0] / away_win_df.shape[0]) * 100, 2)
    else:
        away_win_percentage = 0

    over_25_df = merged_df[merged_df['over_25'] == 1]
    over_25_len = len(over_25_df)
    if not over_25_df.empty:
        over_25_percentage = round(
            (over_25_df[over_25_df['Host_SC'] + over_25_df['Guest_SC'] > 1.5].shape[0] / over_25_df.shape[0]) * 100, 2)
    else:
        over_25_percentage = 0

    under_25_df = merged_df[merged_df['under_25'] == 1]
    under_25_len = len(under_25_df)
    if not under_25_df.empty:
        under_25_percentage = round(
            (under_25_df[under_25_df['Host_SC'] + under_25_df['Guest_SC'] < 3.5].shape[0] / under_25_df.shape[0]) * 100,
            2)
    else:
        under_25_percentage = 0

    btts_df = merged_df[merged_df['btts'] == 1]
    btts_len = len(btts_df)
    if not btts_df.empty:
        btts_percentage = round(
            (btts_df[(btts_df['Host_SC'] > 0.5) & (btts_df['Guest_SC'] > 0.5)].shape[0] / btts_df.shape[0]) * 100, 2)
    else:
        btts_percentage = 0

    home_over_15_df = merged_df[merged_df['home_over_15'] == 1]
    home_over_15_len = len(home_over_15_df)
    if not home_over_15_df.empty:
        home_over_15_percentage = round(
            (home_over_15_df[home_over_15_df['Host_SC'] > 0.5].shape[0] / home_over_15_df.shape[0]) * 100, 2)
    else:
        home_over_15_percentage = 0

    away_over_15_df = merged_df[merged_df['away_over_15'] == 1]
    away_over_15_len = len(away_over_15_df)
    if not away_over_15_df.empty:
        away_over_15_percentage = round(
            (away_over_15_df[away_over_15_df['Guest_SC'] > 0.5].shape[0] / away_over_15_df.shape[0]) * 100, 2)
    else:
        away_over_15_percentage = 0

    home_draw_df = merged_df[merged_df['home_draw'] == 1]
    home_draw_len = len(home_draw_df)
    if not home_draw_df.empty:
        home_draw_percentage = round(
            (home_draw_df[home_draw_df['Host_SC'] >= home_draw_df['Guest_SC']].shape[0] / home_draw_df.shape[0]) * 100,
            2)
    else:
        home_draw_percentage = 0

    away_draw_df = merged_df[merged_df['away_draw'] == 1]
    away_draw_len = len(away_draw_df)
    if not away_draw_df.empty:
        away_draw_percentage = round(
            (away_draw_df[away_draw_df['Host_SC'] <= away_draw_df['Guest_SC']].shape[0] / away_draw_df.shape[0]) * 100,
            2)
    else:
        away_draw_percentage = 0

    print("Saving the data")
    # Get or create the object based on the date
    betting_stat, created = BettingStats.objects.get_or_create(
        date=yesterday_date,
        defaults={
            'average': average,
            'describe': describe,
            'variance': variance,
            'standard_deviation': standard_deviation,
            'home_win_len': home_win_len,
            'home_win_percentage': home_win_percentage,
            'away_win_len': away_win_len,
            'away_win_percentage': away_win_percentage,
            'over_25_len': over_25_len,
            'over_25_percentage': over_25_percentage,
            'under_25_len': under_25_len,
            'under_25_percentage': under_25_percentage,
            'btts_len': btts_len,
            'btts_percentage': btts_percentage,
            'home_over_15_len': home_over_15_len,
            'home_over_15_percentage': home_over_15_percentage,
            'away_over_15_len': away_over_15_len,
            'away_over_15_percentage': away_over_15_percentage,
            'home_draw_len': home_draw_len,
            'home_draw_percentage': home_draw_percentage,
            'away_draw_len': away_draw_len,
            'away_draw_percentage': away_draw_percentage
        }
    )

    if not created:
        # If the object was not created, it means it already exists, so update it
        betting_stat.average = average
        betting_stat.describe = describe
        betting_stat.variance = variance
        betting_stat.standard_deviation = standard_deviation
        betting_stat.home_win_len = home_win_len
        betting_stat.home_win_percentage = home_win_percentage
        betting_stat.away_win_len = away_win_len
        betting_stat.away_win_percentage = away_win_percentage
        betting_stat.over_25_len = over_25_len
        betting_stat.over_25_percentage = over_25_percentage
        betting_stat.under_25_len = under_25_len
        betting_stat.under_25_percentage = under_25_percentage
        betting_stat.btts_len = btts_len
        betting_stat.btts_percentage = btts_percentage
        betting_stat.home_over_15_len = home_over_15_len
        betting_stat.home_over_15_percentage = home_over_15_percentage
        betting_stat.away_over_15_len = away_over_15_len
        betting_stat.away_over_15_percentage = away_over_15_percentage
        betting_stat.home_draw_len = home_draw_len
        betting_stat.home_draw_percentage = home_draw_percentage
        betting_stat.away_draw_len = away_draw_len
        betting_stat.away_draw_percentage = away_draw_percentage
        betting_stat.save()
