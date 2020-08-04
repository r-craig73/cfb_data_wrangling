# cfb_analysis :football:

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/cfb_analysis

## Description
###  Two Python scripts that request and save college football (CFB) stats as JSON files from api.collegefootballdata.com.

* cfb_regular_season_json_import.py: A script that requests regular season stats (general and detailed) and vegas lines for a particular year from api.collegefootballdata.com.  Results are saved as JSON files.  Detailed JSON files are sorted by game ID number (> 800 games/season).
* cfb_post_season_json_import.py: A script that requests post season stats (general and detailed) and vegas lines from api.collegefootballdata.com.  Results are saved as JSON files.  Detailed JSON files are sorted by game ID number (> 40 games/season).

### User can run the script by running...
* (PowerShell Terminal) ```>py .\cfb_regular_season_json_import.py```
* (PowerShell Terminal) ```>py .\cfb_post_season_json_import.py```

Pros | Cons 
-----| -----
The scripts works. | Creating detailed game JSONs takes a while (from 5 to 45 minutes).
--   | Smelly code.

### Technologies Used
* ```Application: Python 3.8.2 32-bit```
* ```Packages: requests, json, and time```

### Things to Do
- [ ] Refactor regular season and post season code to one script.
- [ ] Create a new script using pandas package to import JSON files to a large DataFrame.
- [ ] Create a private repository to analyze the DataFrame.
