import numpy as np;
import pandas as pd;


#
# Python script to demonstrate how to fetch data from the `games`, `plays`, `players`, and `tackles` dataframes.
# No weekly tracking data is used.
#


#
# Load high-level data
#

games 	= pd.read_csv('games.csv');
plays 	= pd.read_csv('plays.csv');
players = pd.read_csv('players.csv');
tackles = pd.read_csv('tackles.csv');


#
# Load weekly intra-game player tracking data
#

week1 = pd.read_csv('tracking_week_1.csv');


#
# Add column to `games` to identify when the home team won.
#

games['homeWin'] = (games['homeFinalScore'] > games['visitorFinalScore']).astype(int);


#
# Fetch 49ers games.
#

games_sf = games.query('(homeTeamAbbr == "SF") or (visitorTeamAbbr == "SF")');
print('49ers Games'); print(games_sf, '\n');


#
# Filter `tackles` dataframe to identify rows pertaining to the 49ers games.
#

tackles_sf = tackles[tackles['gameId'].isin(games_sf['gameId'])];
print('49ers Tackles'); print(tackles_sf, '\n');


#
# Filter `plays` dataframe to identify plays from 49ers games.
#

plays_sf = plays[plays['gameId'].isin(games_sf['gameId'])];
print('49ers Plays'); print(plays_sf, '\n');



#
# Partition `plays_sf` into 49ers offensive and defensive plays.
#

plays_sf_offense = plays_sf.query('possessionTeam == "SF"');
plays_sf_defense = plays_sf.query('defensiveTeam == "SF"');

print('49ers Offensive Plays'); print(plays_sf_offense, '\n');
print('49ers Defensive Plays'); print(plays_sf_defense, '\n');


#
# Identify 49ers tackling events.
#

tackles_sf = tackles[tackles['playId'].isin(plays_sf_defense['playId'])];


#
# Filter `players` for 49ers offensive and defensive players.
#

players_sf_offense = players[players['nflId'].isin(plays_sf_offense['ballCarrierId'])];
players_sf_defense = players[players['nflId'].isin(tackles_sf['nflId'])];

print('49ers Offensive Players'); print(players_sf_offense, '\n');
print('49ers Defensive Players'); print(players_sf_defense, '\n');



#
# Create a list containing the `nflId` for all 49ers players.
#

nflId_sf = list(players_sf_offense) + list(players_sf_defense);



#
# Fetch plays from week 1 49ers/Bears game
# https://www.espn.com/nfl/game?gameId=401437647
#

plays1_sf = plays_sf[plays_sf['gameId'].isin(games_sf.query('week==1')['gameId'])];


#
# Identify week 1 tracking data for 49ers/Bears game
#

tracking1_sf = week1[week1['gameId'].isin(games_sf['gameId'])];