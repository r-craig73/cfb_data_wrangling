import pandas as pd
import requests, json, os

# create list of files within a folder
path = 'temp_2018/'
file_list = os.listdir(path)
print(file_list)

df = pd.read_json('temp_2018/detailedGameStatsCFB-postseason-401032055.json')
print(df)
print(df.dtypes)