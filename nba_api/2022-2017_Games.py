import pandas as pd
import numpy as np
import time

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, teamestimatedmetrics, teamdashboardbygeneralsplits

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


nba_teams = teams.get_teams()



def get_games_dict(nba_teams):
    games_23_dict = {}
    for index, team in enumerate(nba_teams):
        gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable = nba_teams[index]['id'])
        all_games = gamefinder.get_data_frames()[0]
        games_23 = all_games[all_games.SEASON_ID.str[-4:] == '2022']
        games_23_dict[team['full_name']] = games_23
    return games_23_dict


