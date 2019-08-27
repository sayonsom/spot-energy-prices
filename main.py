import requests
import pandas as pd
from bs4 import BeautifulSoup

    
class HTML_table_to_dataframe:
   
    def scrape(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        # soup = BeautifulSoup(open(url), "html.parser")
        return soup.find("table",{"class":"t4 simpletable2"})  

    def make_df(self, table):
        n_columns = 0
        n_rows=0
        column_names = []

        df = pd.DataFrame({'Region' : [], 'Spot Price': [], 'Spark Spread': []})

        for row in table.find_all('tr'):
            cols = row.find_all('td') # Data type = List of bs4.element.tag 
            cols = [c.string for c in cols]
            if len(cols) == 6:
                 df = df.append(pd.Series([cols[0], cols[3], cols[5]], index=['Region','Spot Price','Spark Spread']), ignore_index=True)
        return df



url = "https://www.eia.gov/todayinenergy/prices.php"
# url = "C:\\Users\\CHANDS3\\Desktop\\eia.html"
t = HTML_table_to_dataframe()
table = t.scrape(url)
x = hp.make_df(table)
print(x)

