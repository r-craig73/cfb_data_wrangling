import requests, json, time

# college football year
CFB_YEAR = 2018

## requests and saves regular season stats
reg = requests.get(f'https://api.collegefootballdata.com/games?year={CFB_YEAR}&seasonType=regular')
basic_game_stats = reg.json()
with open(f'cfb_json_{CFB_YEAR}\\basicGameStatsCFB-JSON-{CFB_YEAR}.json', 'w') as f:
    json.dump(basic_game_stats, f)

## list games ID, greater 800 regular season games
reg_cfb_game_id = []
for i in range(0, len(basic_game_stats), 1):
    reg_cfb_game_id.append(basic_game_stats[i]['id'])
print(f'{CFB_YEAR} Regular season games: {len(basic_game_stats)}')

## requests and saves regular season's vegas lines
line = requests.get(f'https://api.collegefootballdata.com/lines?year={CFB_YEAR}&seasonType=regular')
vegas_lines = line.json()
with open(f'cfb_json_{CFB_YEAR}\\vegasLines.json', 'w') as f:
    json.dump(vegas_lines, f)

## requests and saves detailed stats for the regular season (takes a loooong time, 15-45 minutes)
for i in range(0, len(basic_game_stats), 1):
    r = requests.get(f'https://api.collegefootballdata.com/games/teams?year={CFB_YEAR}&seasonType=regular&gameId={reg_cfb_game_id[i]}')
    detailed_game_stats = r.json()
    with open(f'cfb_json_{CFB_YEAR}\\detailedGameStats-{reg_cfb_game_id[i]}.json', 'w') as f:
        json.dump(detailed_game_stats, f)
    time.sleep(3)
