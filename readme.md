# :football: :chart_with_upwards_trend: cfb_data_wrangling :chart_with_downwards_trend: :football:

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/cfb_data_wrangling

## Description
### A project requesting and downloading college football (CFB) stats from [College Football Data API](https://api.collegefootballdata.com/api/docs/?url=/api-docs.json) as JSON files. Data wrangling practice to manipulate JSON file stats into DataFrames for a season (regular & postseason).

File | Description 
-----| -----
cfb_season_json_import.py | Python script that requests JSON files from [College Football Data API](https://api.collegefootballdata.com/api/docs/?url=/api-docs.json). The JSON files will contain stats from a year (general and/or detailed stats;  regular and/or post-season game, and Vegas Lines). Detailed JSON files are sorted by game ID number (over 880 games/season). An [API key is required](https://collegefootballdata.com/key) to run the script.
cfb_stats_jsons_to_dataframe.ipymb (coming soon) | Jupyter notebook file that organizes (or data wrangle) imported JSON files into a large DataFrame for a particular collge football year (hopefully multiple years).

Pros | Cons 
-----| -----
The Python script works. | Downloading detailed JSON regular season stats for each week could take a while (1-2 minutes).
--   | Smelly code.

### Technologies Used
* ```Applications: Anaconda Navigator 2.6.2, Spyder 5.5.1, Python 3.12.4, Jupyter 7.0.8, git 2.45.2, and macOS Terminal```
* ```Python Script Packages: requests and json```
* ```Jupyter Notebook Packages: json, pandas, and numpy```

### Things to Do
- [x] Refactor regular season and post season JSON import code to one script.
- [ ] Create a Jupyter notebook to read various JSON files into a large DataFrame.
- [ ] Create a private repository using scripts and/or Jupyter notebooks to analyze the DataFrame.
