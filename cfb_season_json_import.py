import requests, json, time

# College football constant variables
CFB_YEAR, GAMES, VEGAS_LINES = 2019, 'games', 'lines'
REGULAR_SEASON, POST_SEASON = 'regular', 'postseason'

## Requests and saves regular/post season stats [games] or Vegas lines [lines]
def cfb_stats(date, metric, season):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}')
    basic_stats = results.json()
    if metric.lower() == 'games':
        with open(f'cfb_JSON_{date}\\basicGameStatsCFB-JSON-{season}-{date}.json', 'w') as f:
            json.dump(basic_stats, f)
    elif metric.lower() == 'lines':
        with open(f'cfb_JSON_{date}\\vegasLinesCFB-JSON-{season}-{date}.json', 'w') as f:
            json.dump(basic_stats, f)

# List games ID, regular season (over 800 games) or post season (around 40 games)
def detailed_cfb_stats(date, metric, season):
    cfb_game_id = []
    regular = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType={season}')
    basic_stats = regular.json()
    for i in range(0, len(basic_stats), 1):
        cfb_game_id.append(basic_stats[i]['id'])
    print(f'{date} {season} total games: {len(basic_stats)}')

    # Requests and saves detailed stats for the regular season (takes a loooong time, 15-45 minutes) #757
    for i in range(0, len(basic_stats), 1):
        r = requests.get(f'https://api.collegefootballdata.com/games/teams?year={date}&seasonType={season}&gameId={cfb_game_id[i]}')
        detailed_game_stats = r.json()
        with open(f'cfb_JSON_{date}\\detailedGameStatsCFB-{season}-{cfb_game_id[i]}.json', 'w') as f:
            json.dump(detailed_game_stats, f)
        time.sleep(2.5)

def main():
    cfb_stats(CFB_YEAR, GAMES, REGULAR_SEASON)
    cfb_stats(CFB_YEAR, GAMES, POST_SEASON)
    cfb_stats(CFB_YEAR, VEGAS_LINES, REGULAR_SEASON)
    cfb_stats(CFB_YEAR, VEGAS_LINES, POST_SEASON)
    detailed_cfb_stats(CFB_YEAR, GAMES, REGULAR_SEASON)
    detailed_cfb_stats(CFB_YEAR, GAMES, POST_SEASON)

if __name__ == "__main__":
    main()