import requests, json, time

# college football year
CFB_YEAR = 2018

# requests and saves postseason stats
post = requests.get(f'https://api.collegefootballdata.com/games?year={CFB_YEAR}&seasonType=postseason')
basic_postseason_game_stats = post.json()
with open(f'cfb_json_{CFB_YEAR}\\basicPostseasonGameStatsCFB-JSON-{CFB_YEAR}.json', 'w') as f:
    json.dump(basic_postseason_game_stats, f)

# list games IDs
post_cfb_game_id = []
for i in range(0, len(basic_postseason_game_stats), 1):
    post_cfb_game_id.append(basic_postseason_game_stats[i]['id'])
print(f'{CFB_YEAR} Postseason games: {len(basic_postseason_game_stats)}')

# requests and saves vegas lines for the post season
line = requests.get(f'https://api.collegefootballdata.com/lines?year={CFB_YEAR}&seasonType=postseason')
vegas_lines = line.json()
with open(f'cfb_json_{CFB_YEAR}\\postseasonVegasLines.json', 'w') as f:
    json.dump(vegas_lines, f)

# requests and saves detailed stats for the post season (takes a long time, 3-4 minutes)
for i in range(0, len(basic_postseason_game_stats), 1):
    r = requests.get(f'https://api.collegefootballdata.com/games/teams?year={CFB_YEAR}&seasonType=postseason&gameId={post_cfb_game_id[i]}')
    detailed_game_stats = r.json()
    with open(f'cfb_json_{CFB_YEAR}\\detailedGameStats-{post_cfb_game_id[i]}.json', 'w') as f:
        json.dump(detailed_game_stats, f)
    time.sleep(5)
