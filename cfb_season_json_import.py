import requests
import json
import constant
service_key = constant.API_KEY

# College football constant variables
CFB_YEAR, GAMES, WEEK, VEGAS_LINES = 2011, 'games', 16, 'lines'
REGULAR_SEASON, POST_SEASON, DIVISION = 'regular', 'postseason', 'fbs'

headers = {
    'accept': 'application/json',
    'Authorization': service_key
}

## Request and saves games, lines, and a list of FBS teams as a JSON file.
## Option 2: (use https://collegefootballdata.com website to download CSV)
def cfb_games(date, metric, season, division):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}&division={division}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}-basicGameStatsCFB-JSON-{season}.json', 'w') as f:
        json.dump(basic_stats, f)
            
def cfb_lines(date, metric, season):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}-vegasLinesCFB-JSON-{season}.json', 'w') as f:
        json.dump(basic_stats, f)
        
def teams_fbs(date):
    results = requests.get(f'https://api.collegefootballdata.com/teams/fbs?year={date}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}-teams-FBS-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# Request seasonal stats
def season_stats(date):
    results = requests.get(f'https://api.collegefootballdata.com/stats/season?year={date}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}-season-stats-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# Request more details stats to each game; filter by each week
def cfb_games_teams(date, week_int, season, division):
    results = requests.get(f'https://api.collegefootballdata.com/games/teams?year={date}&week={week_int}&seasonType={season}&classification={division}', 
                           headers=headers)
    basic_stats = results.json()
    with open(f'{date}-{season}-{week_int}-detailedGamesCFB-JSON.json', 'w') as f:
        json.dump(basic_stats, f)

# OPTIONAL
# game/box/advanced
# https://api.collegefootballdata.com/game/box/advanced?gameId=401551469

# stats/game/advanced
# https://api.collegefootballdata.com/stats/game/advanced?year=2022&week=2&seasonType=regular


def main():
    # cfb_games(CFB_YEAR, GAMES, REGULAR_SEASON, DIVISION)
    # cfb_games(CFB_YEAR, GAMES, POST_SEASON, DIVISION)
    # cfb_lines(CFB_YEAR, VEGAS_LINES, REGULAR_SEASON)
    # cfb_lines(CFB_YEAR, VEGAS_LINES, POST_SEASON)
    teams_fbs(CFB_YEAR)
    # season_stats(CFB_YEAR)
    #cfb_games_teams(CFB_YEAR, WEEK, REGULAR_SEASON, DIVISION)

if __name__ == "__main__":
    main()