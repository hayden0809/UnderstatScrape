import pandas as pd
import understatapi

# This is for scraping
import re
import requests
import json
from bs4 import BeautifulSoup

response = requests.get('https://understat.com/match/26651')
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
ugly_soup = str(soup)

shots_data = re.search("var shotsData .*= JSON.parse\('(.*)'\)", ugly_soup).group(1)
data = shots_data.encode('utf8').decode('unicode_escape')
data = json.loads(data)
print(data)






# This is using the understat api

# client = understatapi.UnderstatClient()

# '''
# Gets the league data for Serie A in 2024
# '''
# league_data = client.league(league='Serie_A').get_match_data(season='2024')
# # print(league_data[0])

# shot_data = client.match(match='27362').get_shot_data()
# # print(shot_data['h'][0])

# player_data = client.player(player='11380').get_shot_data()
# df = pd.DataFrame(player_data)
# print(df.head())