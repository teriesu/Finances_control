import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from utils import Utils

class FinViz_scraper:

    def __init__(self):
        self.utils = Utils()
        self.companie_names = self.utils.read_companies(columns = 'CompID')
        self.prices = pd.DataFrame()

    def get_values(self):

        for add in self.companie_names:

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
                self.prices = self.prices.append(action_value, ignore_index=True)
                # return action_value

            except Exception as e:
                return e
            self.prices['CompID'] = self.companie_names
        return self.prices

    def actValue(self, id):

        url = f'https://finviz.com/quote.ashx?t={id}'
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
            action_value = action_value.tolist()

        except Exception as e:
            return e

        return float(action_value[0])
