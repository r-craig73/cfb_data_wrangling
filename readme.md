# cfb_analysis :football:

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/cfb_analysis

## Description
### A Python script that requests college football (CFB) stats as JSON files from api.collegefootballdata.com.
### Coming soon: A Python script that stores various CFB stats into a large DataFrame.

* cfb_season_json_import.py: A script requesting a CFB season of stats (general and detailed, regular and post-season game) and CFB vegas lines from api.collegefootballdata.com.  Results are saved as JSON files.  Detailed JSON files are sorted by game ID number (over 880 games/season). An API key is required to run the script.
* cfb_data_dataframe_setup.py (coming soon): A script that organize CFB stats into a large DataFrame.

Pros | Cons 
-----| -----
The scripts works. | Creating detailed JSON regular season stats takes a while (about 15-45 minutes).
--   | Smelly code.

### Technologies Used
* ```Application: Python 3.12.4```
* ```Packages: requests and json```

### Things to Do
- [x] Refactor regular season and post season JSON import code to one script.
- [ ] Create a new script using pandas package to import JSON files to a large DataFrame.
- [ ] Create a private repository using other packages to analyze the DataFrame.
