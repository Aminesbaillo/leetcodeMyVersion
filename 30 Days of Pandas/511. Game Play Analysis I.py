import pandas as pd 

data = {
    "player_id": [1, 1, 2, 3, 3],
    "device_id": [2, 2, 3, 1, 4],
    "event_date": ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"],
    "games_played": [5, 6, 1, 0, 5],
}

data = pd.DataFrame(data = data) 
print(data)

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    """
    Analyze the activity table to generate a new table with the player_id, 
    device_id, the date of the first login, the number of days since the first
    login, and the number of games player in the last 30 days.

    Parameters
    ----------
    activity : pd.DataFrame
        The DataFrame containing the activity data

    Returns
    -------
    pd.DataFrame
        The DataFrame containing the results of the analysis
    """
    activity = activity.sort_values(by = 'event_date', ascending = True).reset_index(drop = True)
    activity.drop_duplicates(subset = 'player_id', keep = 'first', inplace = True)
    activity.rename(columns = {'event_date' : 'first_login'}, inplace = True)
    return activity[['player_id', 'first_login']]

print(game_analysis(data))