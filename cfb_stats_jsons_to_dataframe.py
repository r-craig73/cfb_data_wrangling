import pandas as pd
import json, os

# create list of files within a folder
# path = 'temp_2018/'
# file_list = os.listdir(path)
# print(file_list)

# importing one JSON file into pandas
df = pd.read_json('temp_2018/detailedGameStatsCFB-postseason-401032055.json')
df2 = pd.read_json('temp_2018/basicGameStatsCFB-JSON-postseason-2018.json')
df3 = pd.read_json('temp_2018/vegasLinesCFB-JSON-postseason-2018.json')

# split df 'DataFrame' into id variable; append id to a (1x2 matrix)
df_id = df.drop(['teams'], axis=1)
df_id = df_id.append({'id' : df.id[0]}, ignore_index=True)

# split df 'DataFrame' into teams overall stats (4 columns)
df_teams = pd.DataFrame(df.teams[0])
df_teams_basic = df_teams.drop(['stats'], axis=1)

# merge df_id and df_teams variables
df_id_teams = pd.concat([df_id, df_teams_basic], axis=1)

# split teams 'DataFrame' into category and stat variables
team_0_stats = pd.DataFrame(df_teams.stats[0]).sort_values(by=['category'])
team_1_stats = pd.DataFrame(df_teams.stats[1]).sort_values(by=['category'])

# join teams stats into a 3xN matrix ('category', 'stat_x', 'stat_y')
teams_detailed_stats = pd.merge(team_0_stats, team_1_stats, how='inner', on=['category']).sort_values(by=['category'])

# transpose teams_detailed_stats 
teams_transposed = teams_detailed_stats.transpose()
teams_transposed = pd.DataFrame(teams_transposed.rename(columns=teams_transposed.iloc[0]).drop(teams_transposed.index[0]))
teams_transposed = teams_transposed.set_index([pd.Index([0, 1])])

# join df_id_teams and teams_detailed_stats DataFrames
teams_final = pd.concat([df_id_teams, teams_transposed], axis=1)

# remove DataFrame variables (regular or postseason games)
df_reduced_series = df2.drop(['attendance', 'away_id', 'away_post_win_prob', 'excitement_index', 'home_id', 'home_post_win_prob', 'start_date', 'start_time_tbd', 'venue', 'venue_id'], axis=1)
df_reduced_vegas_lines = df3.drop(['season', 'seasonType', 'week', 'homeConference', 'homeScore', 'awayScore', 'awayConference'], axis=1)
# search for matching id, game
id_basic_game = df_reduced_series.loc[df_reduced_series['id'] == df.id[0]]

# search for matching id, vegas line
id_vegas_line = df_reduced_vegas_lines.loc[df_reduced_vegas_lines['id'] == df.id[0]]

# place lines in a Nx4 DataFrame, sort by provider
vegas_lines = pd.DataFrame(id_vegas_line.iloc[0, 3])

# pivot vegas_lines and sort by OverUnder and Spread
lines_over_under = vegas_lines.pivot(columns='provider', values='overUnder').rename(columns={'Caesars': 'CaesarsOverUnder', 'consensus': 'consenusOverUnder', 'numberfire': 'numberfireOverUnder', 'teamrankings': 'teamrankingsOverUnder'}).fillna(method='bfill').fillna(method='ffill')
lines_formatted_spread = vegas_lines.pivot(columns='provider', values='formattedSpread').rename(columns={'Caesars': 'CaesarsSpread', 'consensus': 'consenusSpread', 'numberfire': 'numberfireSpread', 'teamrankings': 'teamrankingsSpread'}).fillna(method='bfill').fillna(method='ffill')
final_lines = pd.concat([lines_over_under.iloc[0:2, :], lines_formatted_spread.iloc[0:2, :]], axis=1)

# place away team in row 0, place home team in row 1
df_away_team = id_basic_game.loc[:, ['id', 'away_conference', 'away_line_scores', 'away_points', 'away_team', 'conference_game', 'neutral_site', 'season', 'season_type', 'week']].rename(columns={'away_conference': 'conference', 'away_line_scores': 'by_quarter_scores', 'away_points': 'points', 'away_team':'team'})
df_home_team = id_basic_game.loc[:, ['id', 'home_conference', 'home_line_scores', 'home_points', 'home_team', 'conference_game', 'neutral_site', 'season', 'season_type', 'week']].rename(columns={'home_conference': 'conference', 'home_line_scores': 'by_quarter_scores', 'home_points': 'points', 'home_team':'team'})

# merge individual game basic results
# place away team in row 0
df_teams_merge = df_away_team

# place home team in row 1 and merge rows into a DataFrame
df_teams_merge = df_teams_merge.append(df_home_team, ignore_index=True)

# create a larger 2xN DataFrame (teams_final and df_teams_merge)
df_game_stats_merge = pd.concat([teams_final, df_teams_merge], axis=1)
final_df = pd.concat([df_game_stats_merge, final_lines], axis=1)

# remove duplates from df_game_stats_merge (To do)

print(teams_final)
print(df_teams_merge)
print(df_game_stats_merge)
# print(len(list(df_game_stats_merge)))
# print(id_vegas_line)
print(vegas_lines)
# print(lines_over_under)
# print(lines_formatted_spread)
print(lines_formatted_spread.iloc[0:2, :])
print(final_lines)
print(final_df)
print(list(final_df))

# for i in range(0, len(list(final_df)), 1):
#     print(list(final_df)[i])

# to do: [x] (1) keep the id value in the first column
# to do: [x] (2) expand teams columns into other columns
# to do: [x] join (1) and (2) to a 2x5 DataFrame
# to do: [x] (3) expand each team detailed stats into other columns, 2xN DataFrame
# to do: [x] (4) join a vegas line game matching the id number of a game (regular or postseason, basic_stats, detailed_stats) , 2xN DataFrame
# to do: [x] join (1), (2), (3), and (4) to a 2xN DataFrame
# to do: [ ] join a game DataFrame matching the id number of a postseason game (postseason, basic_stats, detailed_stats), 2xN DataFrame
# to do: [ ] join a game DataFrame matching the id number of a regular game (regular, basic_stats, detailed_stats), 2xN DataFrame

