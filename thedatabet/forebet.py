import os
import json
import urllib
from datetime import datetime, timedelta

from unidecode import unidecode
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from django.conf import settings

from wagtail.documents.models import Document

from .models import BettingTips


def main():

    # Getting file
    file = Document.objects.get(id=1).file

    # Reading and loading the file
    file_contents = file.read()
    data = json.loads(file_contents.decode('utf-8'))


    keys = list(data[-1].keys())
    last_day = keys[0]

    last_date_string = last_day
    date_obj = datetime.strptime(last_date_string, '%Y-%m-%d')

    # Add one day to the date
    next_day = date_obj + timedelta(days=1)

    # Format the next day as a string
    next_day_string = next_day.strftime('%Y-%m-%d')

    start_year, start_month, start_day = map(int, next_day_string.split('-'))

    # Get today's date
    today_date = datetime.now()

    # Subtract two days to get "the day before yesterday"
    yesterday_date = today_date - timedelta(days=1)

    # Format today's date as a string in 'YYYY-MM-DD' format
    formatted_date = yesterday_date.strftime('%Y-%m-%d')

    end_year, end_month, end_day = map(int, formatted_date.split('-'))

    start_date = datetime(start_year, start_month, start_day)
    # end_date = start_date + timedelta(days=4)
    end_date = datetime(end_year, end_month, end_day)
    delta = timedelta(days=1)


    while start_date <= end_date:
        date_str = start_date.strftime("%Y-%m-%d")
        url = f'https://www.forebet.com/scripts/getrs.php?ln=en&tp=1x2&in={date_str}&ord=0&tz=+120'
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
        string_response = urllib.request.urlopen(req).read().decode('utf-8')
        response = json.loads(string_response)
        data.append({date_str: response})
        start_date += delta

    file_path = os.path.join(settings.MEDIA_ROOT, 'documents/forebet_data.json')

        # Save data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(data, f)

    print("Data saved to forebet_data.json")


    # New function
    with open(file_path, 'r') as file:
        data = json.load(file)
    games_array = []

    # Iterate over each match day in the data
    for match_day in data:
        # Iterate over each date within the match day
        for date, data_for_date in match_day.items():
            # Extract the games for the current date
            games_for_date = data_for_date[0]
            # Append the games to the games_array
            games_array.extend(games_for_date)

    # Calculate the length of games_array
    num_games = len(games_array)
    print("Number of games:", num_games)

    games_df = pd.DataFrame(games_array,
                            columns=["DATE_BAH", "league_id", "Pred_1", "Pred_X", "Pred_2", "host_id", "guest_id",
                                     "HOST_NAME", "GUEST_NAME", "Host_SC", "Guest_SC", "host_sc_pr", "guest_sc_pr",
                                     "goalsavg"])
    # Remove rows with null values
    games_df.dropna(inplace=True)

    print("Creating A Dataframe")

    # New function
    games_df["DATE_BAH"] = games_df["DATE_BAH"].astype("datetime64[ns]")
    games_df["league_id"] = games_df["league_id"].astype("int16")
    games_df["host_id"] = games_df["host_id"].astype("int16")
    games_df["guest_id"] = games_df["guest_id"].astype("int16")
    games_df["Host_SC"] = games_df["Host_SC"].astype("int16")
    games_df["Guest_SC"] = games_df["Guest_SC"].astype("int16")
    games_df["Pred_1"] = games_df["Pred_1"].astype("int16")
    games_df["Pred_X"] = games_df["Pred_X"].astype("int16")
    games_df["Pred_2"] = games_df["Pred_2"].astype("int16")
    games_df["goalsavg"] = games_df["goalsavg"].astype("float16")
    games_df["host_sc_pr"] = games_df["host_sc_pr"].astype("int16")
    games_df["guest_sc_pr"] = games_df["guest_sc_pr"].astype("int16")
    # Remove outliers
    games_df = games_df[(games_df['Host_SC'] <= 8) & (games_df['Guest_SC'] <= 8)]
    # Replace special characters in specific columns
    games_df['HOST_NAME'] = games_df['HOST_NAME'].apply(lambda x: unidecode(x))
    games_df['GUEST_NAME'] = games_df['GUEST_NAME'].apply(lambda x: unidecode(x))

    print("Changing Datatypes")

    # Match result
    games_df['result'] = np.select(
        [games_df['Host_SC'] > games_df['Guest_SC'], games_df['Host_SC'] == games_df['Guest_SC'],
         games_df['Host_SC'] < games_df['Guest_SC']], [1, 2, 3])

    print("Putting Match result")


    # Sort the DataFrame by date if it's not already sorted
    games_df.sort_values(by='DATE_BAH', inplace=True)

    # Calculate the rolling average of the last 5 games for each team using 'Host_SC'
    games_df['Host_Perfom'] = games_df.groupby('host_id')['Host_SC'].rolling(window=5,
                                                                             min_periods=1).mean().reset_index(level=0,
                                                                                                               drop=True)

    # Calculate the rolling average of goals scored against the team (host_id) when playing at home
    games_df['Host_Concede'] = games_df.groupby('host_id')['Guest_SC'].rolling(window=5,
                                                                               min_periods=1).mean().reset_index(
        level=0, drop=True)

    # Calculate the rolling average of the last 5 games for each team using 'Guest_SC'
    games_df['Guest_Perfom'] = games_df.groupby('guest_id')['Guest_SC'].rolling(window=5,
                                                                                min_periods=1).mean().reset_index(
        level=0, drop=True)

    # Calculate the rolling average of goals scored against the team (guest_id) when playing away
    games_df['Guest_Concede'] = games_df.groupby('guest_id')['Host_SC'].rolling(window=5,
                                                                                min_periods=1).mean().reset_index(
        level=0, drop=True)

    # If you want to fill NaN values with 0 for the first 4 rows, you can use fillna(0)
    games_df['Host_Perfom'] = games_df['Host_Perfom'].fillna(0)
    games_df['Guest_Perfom'] = games_df['Guest_Perfom'].fillna(0)
    games_df['Host_Concede'] = games_df['Host_Concede'].fillna(0)
    games_df['Guest_Concede'] = games_df['Guest_Concede'].fillna(0)

    # Now df contains a new column 'avg_goals_last_5_games' with the average goals of the last 5 games for each row
    print("Host_Perfom, Guest_Perfom, Host_Concede & Guest_Concede")



    # Define features and target variable
    features = games_df.drop(columns=["Host_SC", "Guest_SC", "HOST_NAME", "GUEST_NAME", "DATE_BAH", "result"])
    target = games_df[["Host_SC", "Guest_SC", "result"]]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

    # Normalize features
    #scaler = StandardScaler()
    #X_train = scaler.fit_transform(X_train)
    #X_test = scaler.transform(X_test)

    # Train separate models for each target variable using RandomForestRegressor
    models = {}
    for column in target.columns:
        model = RandomForestRegressor(random_state=42, max_depth=10, min_samples_split=2, min_samples_leaf=1)
        model.fit(X_train, y_train[column])
        models[column] = model

    # Make predictions
    predictions = {}
    for column, model in models.items():
        predictions[column] = model.predict(X_test)

        # Evaluate using regression metrics
    regression_metrics = {}
    for column in target.columns:
        mse = mean_squared_error(y_test[column], predictions[column])
        r2 = r2_score(y_test[column], predictions[column])
        regression_metrics[column] = {'Mean Squared Error': mse, 'R-squared': r2}

    print("Regression metrics:")
    for column, metrics in regression_metrics.items():
        print(f"{column}:")
        for metric_name, value in metrics.items():
            print(f"  {metric_name}: {value}")

    # Make predictions and put them back into games_df
    for column, model in models.items():
        games_df[f"Predicted_{column}"] = model.predict(features)

    print("Machine Learning")


    # Get today's date
    today = datetime.now()

    # Calculate the date for the next day
    next_day = today + timedelta(days=1)

    # Format the date in the required format (YYYY-MM-DD)
    next_day_str = next_day.strftime('%Y-%m-%d')

    # Construct the URL with the next day's date
    url = f'https://www.forebet.com/scripts/getrs.php?ln=en&tp=1x2&in={next_day_str}&ord=0&tz=+120'

    new_req = urllib.request.Request(url)
    new_req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    new_string_response = urllib.request.urlopen(new_req).read().decode('utf-8')
    new_r = json.loads(new_string_response)

    print("Next Day Forebet data")

    new_games = new_r[0]
    new_leagues = new_r[1]

    new_games_df = pd.DataFrame(new_games,
                                columns=["DATE_BAH", "league_id", "Pred_1", "Pred_X", "Pred_2", "host_id", "guest_id",
                                         "HOST_NAME", "GUEST_NAME", "Host_SC", "Guest_SC", "host_sc_pr", "guest_sc_pr",
                                         "goalsavg"])
    # List of columns you want to check for null values
    # columns_to_check = ['Host_SC', 'Guest_SC', 'Host_SC_HT', 'Guest_SC_HT']

    # Remove rows with null values in the selected columns
    # new_games_df.dropna(subset=columns_to_check, inplace=True)

    # Check for null values in each column

    # Add league and Country in the dataframe
    new_leagues_df = pd.DataFrame(new_leagues)
    column_name = new_leagues_df.columns[0]
    first_row_value = new_leagues_df.iloc[1][column_name]
    new_games_df["country"] = new_games_df["league_id"].map(new_leagues_df.iloc[0])
    new_games_df["league"] = new_games_df["league_id"].map(new_leagues_df.iloc[1])

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
    # Replace special characters in specific columns
    new_games_df['HOST_NAME'] = new_games_df['HOST_NAME'].apply(lambda x: unidecode(x))
    new_games_df['GUEST_NAME'] = new_games_df['GUEST_NAME'].apply(lambda x: unidecode(x))

    print("New games dataframe")

    for index, row in new_games_df.iterrows():
        host_id = row['host_id']
        guest_id = row['guest_id']
        # Filter rows in games_df for the current host_id and guest_id
        host_rows = games_df[games_df['host_id'] == host_id]
        guest_rows = games_df[games_df['guest_id'] == guest_id]

        # Check if there are matching rows and if not, assign NaN or any default value
        host_perfom = host_rows['Host_Perfom'].iloc[-1] if not host_rows.empty else None
        host_concede = host_rows['Host_Concede'].iloc[-1] if not host_rows.empty else None
        guest_perfom = guest_rows['Guest_Perfom'].iloc[-1] if not guest_rows.empty else None
        guest_concede = guest_rows['Guest_Concede'].iloc[-1] if not guest_rows.empty else None

        # Assign the performance data to the corresponding rows in new_games_df
        new_games_df.at[index, 'Host_Perfom'] = host_perfom
        new_games_df.at[index, 'Host_Concede'] = host_concede
        new_games_df.at[index, 'Guest_Perfom'] = guest_perfom
        new_games_df.at[index, 'Guest_Concede'] = guest_concede

    # Drop rows with null values in 'Host_Perfom' and 'Guest_Perfom' columns
    new_games_df.dropna(subset=['Host_Concede', 'Guest_Concede'], inplace=True)
    # Drop rows with null values in 'Host_Perfom' and 'Guest_Perfom' columns
    new_games_df.dropna(subset=['Host_Perfom', 'Guest_Perfom'], inplace=True)


    print("New games Host_Perfom, Guest_Perfom, Host_Concede & Guest_Concede")

    # Assuming new_games_df is your new DataFrame containing the data to be predicted

    # Preprocess the new DataFrame by dropping unnecessary columns
    new_features = new_games_df.drop(
        columns=["Host_SC", "Guest_SC", "HOST_NAME", "GUEST_NAME", "DATE_BAH", "country", "league"])

    # Make predictions using the trained models
    for column, model in models.items():
        new_games_df[f"Predicted_{column}"] = model.predict(new_features)

    # Now, new_games_df contains the predicted values in the "Predicted_Host_SC" and "Predicted_Guest_SC" columns

    print("Convert to 2 decimal places")
    # Round specific float columns to two decimal places
    new_games_df['Predicted_Host_SC'] = new_games_df['Predicted_Host_SC'].round(2)
    new_games_df['Predicted_Guest_SC'] = new_games_df['Predicted_Guest_SC'].round(2)
    new_games_df['Predicted_result'] = new_games_df['Predicted_result'].round(2)
    new_games_df['Host_Perfom'] = new_games_df['Host_Perfom'].round(2)
    new_games_df['Host_Concede'] = new_games_df['Host_Concede'].round(2)
    new_games_df['Guest_Perfom'] = new_games_df['Guest_Perfom'].round(2)
    new_games_df['Guest_Concede'] = new_games_df['Guest_Concede'].round(2)
    #new_games_df['goalsavg'] = new_games_df['goalsavg'].round(2)

    print("New games predictions")

    new_games_df["home_win"] = np.where(
        (new_games_df['Predicted_Host_SC'] > (new_games_df['Predicted_Guest_SC'] + 1)) &
        (new_games_df['Predicted_result'] < 1.6) &
        (new_games_df['host_sc_pr'] > new_games_df['guest_sc_pr']) &
        (new_games_df['Host_Perfom'] < new_games_df['Guest_Concede']),
        1, 0)

    new_games_df["away_win"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + 1) < new_games_df['Predicted_Guest_SC']) &
        (new_games_df['Predicted_result'] > 2.2) &
        (new_games_df['host_sc_pr'] < new_games_df['guest_sc_pr']) &
        (new_games_df['Guest_Perfom'] < new_games_df['Host_Concede']),
        1, 0)

    new_games_df["over_25"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + new_games_df['Predicted_Guest_SC']) > 3) &
        ((new_games_df['host_sc_pr'] + new_games_df['guest_sc_pr']) > 2) &
        (new_games_df['goalsavg'] > 2.5) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] + new_games_df['Guest_Perfom'] + new_games_df[
            'Guest_Concede']) > 5),
        1, 0)

    new_games_df["under_25"] = np.where(
        ((new_games_df['Predicted_Host_SC'] + new_games_df['Predicted_Guest_SC']) < 1.5) &
        ((new_games_df['host_sc_pr'] + new_games_df['guest_sc_pr']) < 2) &
        (new_games_df['goalsavg'] < 2) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] +
          new_games_df['Guest_Perfom'] + new_games_df['Guest_Concede']) < 5),
        1, 0
    )

    new_games_df["btts"] = np.where(
        (new_games_df['Predicted_Host_SC'] > 1.5) & (new_games_df['Predicted_Guest_SC'] > 1.5) &
        (new_games_df['host_sc_pr'] > 0) & (new_games_df['guest_sc_pr'] > 0) &
        (new_games_df['goalsavg'] > 3) &
        (new_games_df['Predicted_result'] >= 1.5) & (new_games_df['Predicted_result'] <= 2.5) &
        ((new_games_df['Host_Perfom'] + new_games_df['Host_Concede'] + new_games_df['Guest_Perfom'] + new_games_df[
            'Guest_Concede']) > 5),
        1, 0
    )

    new_games_df["home_over_15"] = np.where(
        (new_games_df['Predicted_Host_SC'] > 2) &
        (new_games_df['host_sc_pr'] > 0) &
        (new_games_df['Predicted_result'] < 1.5) &
        (new_games_df['Host_Perfom'] > 1.5) &
        (new_games_df['Guest_Concede'] > 1.5),
        1, 0
    )

    new_games_df["away_over_15"] = np.where(
        (new_games_df['Predicted_Guest_SC'] > 2) &
        (new_games_df['guest_sc_pr'] > 0) &
        (new_games_df['Predicted_result'] > 2.4) &
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

    print("Markets for new games")

    string_new_games_df_json = new_games_df.to_json(orient="records")
    new_games_df_json = json.loads(string_new_games_df_json)

    print(type(new_games_df_json))

    BettingTips.objects.create(
        date=next_day,
        games=new_games_df_json,
        host_sc_mse=regression_metrics['Host_SC']['Mean Squared Error'],
        host_sc_r2=regression_metrics['Host_SC']['R-squared'],
        guest_sc_mse=regression_metrics['Guest_SC']['Mean Squared Error'],
        guest_sc_r2=regression_metrics['Guest_SC']['R-squared'],
        result_mse=regression_metrics['result']['Mean Squared Error'],
        result_r2=regression_metrics['result']['R-squared'],
    )

    print("Betting tips and regression metrics saved.")






