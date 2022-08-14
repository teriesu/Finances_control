import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from utils import Utils

class FinViz_scraper:

    def get_value(self):
        utils = Utils()
        companie_names = utils.read_companies(columns = 'CompID')
        prices = pd.DataFrame()
        for add in companie_names:

            url = f'https://finviz.com/quote.ashx?t={add}'
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            html = soup(webpage, "html.parser")

            try:
                # Find fundamentals table
                fundamentals = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]

                fundamentals.columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                colOne = []
                colLength = len(fundamentals)
                for k in np.arange(0, colLength, 2):
                    colOne.append(fundamentals[f'{k}'])
                attrs = pd.concat(colOne, ignore_index=True)

                colTwo = []
                colLength = len(fundamentals)
                for k in np.arange(1, colLength, 2):
                    colTwo.append(fundamentals[f'{k}'])
                vals = pd.concat(colTwo, ignore_index=True)

                fundamentals = pd.DataFrame()
                fundamentals['Attributes'] = attrs
                fundamentals['ActValue'] = vals
                fundamentals = fundamentals.set_index('Attributes')
                action_value = fundamentals.loc['Price']
                # print(action_value.head())
                prices = prices.append(action_value, ignore_index=True)
                # return action_value

            except Exception as e:
                return e
            prices['CompID'] = companie_names
        return prices
