import requests, json, time

# College football constant variables
CFB_YEAR, GAMES, VEGAS_LINES = 2018, 'games', 'lines'

## Requests and saves regular season stats [games] or Vegas lines [lines]
def cfb_stats(date, metric):
    results = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType=regular')
    basic_stats = results.json()
    if metric.lower() == 'games':
        with open(f'cfb_json_{date}\\basicGameStatsCFB-JSON-{date}.json', 'w') as f:
            json.dump(basic_stats, f)
    elif metric.lower() == 'lines':
        with open(f'cfb_json_{date}\\vegasLines-{date}.json', 'w') as f:
            json.dump(basic_stats, f)

# List games ID, greater than 800 regular season games
def detailed_cfb_stats(date, metric):
    regular_cfb_game_id = []
    regular = requests.get(f'https://api.collegefootballdata.com/{metric}?year={date}&seasonType=regular')
    basic_stats = regular.json()
    for i in range(0, len(basic_stats), 1):
        regular_cfb_game_id.append(basic_stats[i]['id'])
    print(f'{date} Regular season games: {len(basic_stats)}')

    # Requests and saves detailed stats for the regular season (takes a loooong time, 15-45 minutes)
    for i in range(0, len(basic_stats), 1):
        r = requests.get(f'https://api.collegefootballdata.com/games/teams?year={date}&seasonType=regular&gameId={regular_cfb_game_id[i]}')
        detailed_game_stats = r.json()
        with open(f'cfb_json_{date}\\detailedGameStats-{regular_cfb_game_id[i]}.json', 'w') as f:
            json.dump(detailed_game_stats, f)
    time.sleep(2.5)

def main():
    cfb_stats(CFB_YEAR, GAMES)
    cfb_stats(CFB_YEAR, VEGAS_LINES)
    detailed_cfb_stats(CFB_YEAR, GAMES)

if __name__ == "__main__":
    main()