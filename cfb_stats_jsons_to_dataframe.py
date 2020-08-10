import pandas as pd
import json, os

# create list of files within a folder
# path = 'temp_2018/'
# file_list = os.listdir(path)
# print(file_list)

# importing one JSON file into pandas
df = pd.read_json('temp_2018/detailedGameStatsCFB-postseason-401032055.json')

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

print(teams_transposed)
print(teams_final)

# to do: [x] (1) keep the id value in the first column
# to do: [x] (2) expand teams columns into other columns
# to do: [x] join (1) and (2) to a 3x5 DataFrame
# to do: [x] (3) expand each team detailed stats into other columns, 3xN DataFrame
# to do: [x] join (1), (2), (3) to a 3xN DataFrame