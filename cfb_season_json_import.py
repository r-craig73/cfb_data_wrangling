import requests
import json
import constant
service_key = constant.API_KEY

# College football constant variables
CFB_YEAR, GAMES, WEEK, VEGAS_LINES = 2024, 'games', 1, 'lines'
REGULAR_SEASON, POST_SEASON, DIVISION = 'regular', 'postseason', 'fbs'

headers = {
    'accept': 'application/json',
    'Authorization': service_key
}

## Request and saves games, lines, and a list of FBS teams as a JSON file.
## Option 2: (use https://collegefootballdata.com website to download CSV)

# Request score and basic stats
def cfb_games(date, metric, season, division):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}&division={division}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-basicGameStatsCFB-JSON-{season}.json', 'w') as f:
        json.dump(basic_stats, f)

# Request Vegas Lines, filtered by year and season (regular & post-season)
def cfb_lines(date, metric, season):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-vegasLinesCFB-JSON-{season}.json', 'w') as f:
        json.dump(basic_stats, f)
 
# Request footbal teams by year
def teams_fbs(date):
    results = requests.get(f'https://api.collegefootballdata.com/teams/fbs?year={date}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-teams-FBS-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# Request seasonal stats by year
def season_stats(date):
    results = requests.get(f'https://api.collegefootballdata.com/stats/season?year={date}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-season-stats-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# Request more details stats for each game; filtered by regular season week, and season (regular & post-season)
def cfb_games_teams(date, week_int, season, division):
    results = requests.get(f'https://api.collegefootballdata.com/games/teams?year={date}&week={week_int}&seasonType={season}&classification={division}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-{season}-{week_int}-detailedGamesCFB-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# Request advanced stats for each game; filtered by regular season week
def stats_game_advanced(date, week_int, season):
    results = requests.get(f'https://api.collegefootballdata.com/stats/game/advanced?year={date}&week={week_int}&seasonType={season}',
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}_cfb_JSON-CSV/{date}-{season}-{week_int}-detailedGamesCFBAdvanced-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# OPTIONAL
# game/box/advanced
# https://api.collegefootballdata.com/game/box/advanced?gameId=401551469

def main():
    # cfb_games(CFB_YEAR, GAMES, REGULAR_SEASON, DIVISION)
    # cfb_games(CFB_YEAR, GAMES, POST_SEASON, DIVISION)
    # cfb_lines(CFB_YEAR, VEGAS_LINES, REGULAR_SEASON)
    # cfb_lines(CFB_YEAR, VEGAS_LINES, POST_SEASON)
    # teams_fbs(CFB_YEAR)
    # season_stats(CFB_YEAR)
    # cfb_games_teams(CFB_YEAR, WEEK, REGULAR_SEASON, DIVISION)
    stats_game_advanced(CFB_YEAR, WEEK, REGULAR_SEASON)

if __name__ == "__main__":
    main()