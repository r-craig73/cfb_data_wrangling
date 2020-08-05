# cfb_analysis :football:

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/cfb_analysis

## Description
###  Two Python scripts that request and save college football (CFB) stats as JSON files from api.collegefootballdata.com.

* cfb_season_json_import.py: A script that requests season stats (general and detailed) and vegas lines for a college college football season from api.collegefootballdata.com.  Results are saved as JSON files.  Detailed JSON files are sorted by game ID number (over 880 games/season).
* cfb_data_dataframe_setup.py (coming soon): A script that organize college football stats into a large DataFrame.

### User can run the script by running...
* (PowerShell Terminal) ```>py .\cfb_season_json_import.py```

Pros | Cons 
-----| -----
The scripts works. | Creating JSON files of detailed regular season stats takes a while (could take 15-45 minutes).
--   | Smelly code.

### Technologies Used
* ```Application: Python 3.8.2 32-bit```
* ```Packages: requests, json, time, and pandas```

### Things to Do
- [x] Refactor regular season and post season JSON import code to one script.
- [ ] Create a new script using pandas package to import JSON files to a large DataFrame.
- [ ] Create a private repository to analyze the DataFrame.
