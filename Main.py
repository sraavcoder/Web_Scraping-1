from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table')
table_rows = table.find_all('tr')
Scraped_Data = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tag.text.rstrip() for tag in td]
    Scraped_Data.append(row)

del Scraped_Data[0]

df = pd.DataFrame(list(Scraped_Data), columns=[
    'V_mag', 'Star_name', 'Bayer_Designation', 'Distance', 'Spectral_class', 'Mass', 'Radius', 'Luminosity'])

df.to_csv('Final.csv')
