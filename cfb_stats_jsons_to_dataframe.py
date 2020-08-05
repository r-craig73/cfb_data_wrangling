import pandas as pd
import requests, json, os

# create list of files within a folder
path = 'temp_2018/'
file_list = os.listdir(path)
# print(file_list)

# importing one JSON file into pandas
df = pd.read_json('temp_2018/detailedGameStatsCFB-postseason-401032055.json')

# split df 'DataFrame' into id
df_id = df.id[0]

# split df 'DataFrame' into teams
df_teams = pd.DataFrame(df.teams[0])

# split teams 'DataFrame' into detailed teams stats
team_0_stats = pd.DataFrame(df_teams.stats[0])
team_1_stats = pd.DataFrame(df_teams.stats[1])

print(df_id)
print(df_teams)
print(team_0_stats)
print(team_1_stats)

# to do: (1) keep the id value in the first column
# to do: (2) expand teams columns into other columns
# to do: (3) expand each team stats into other columns
# to do: join (1), (2), (3) into a 2 x N DataFrame