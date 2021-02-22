from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table')
table_rows = table.find_all('tr')
temp_list = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tag.text.rstrip() for tag in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius, Lum)), columns=[
    'Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])

df.to_csv('Final.csv')
