import pandas as pd

class Utils:

    def read_companies(self, columns = None):
        companies = pd.read_csv('Data/companies.csv')
        if columns is None:
            return companies
        else:
            compCol= companies[columns]
            return compCol

    def calcProffit(self, compData, compActData, benefitIntent = 0.2):

        profitTable = pd.DataFrame()
        profitTable['Action'] = compData['Name']
        profitTable['CompID'] = compActData['CompID']
        profitTable['StartInvest'] = compData['StartInvest']
        compActData['ActValue'] = compActData['ActValue'].astype(float)
        profitTable['ActInvest'] =  compData['StartInvest'] * compActData['ActValue'] / compData['StartValue']
        profitTable['Benefit'] = profitTable['ActInvest'] - compData['StartInvest']
        trybenefict = compData['StartInvest']*benefitIntent
        profitTable['percent'] = (100*profitTable['ActInvest']/compData['StartInvest'])-100
        profitTable['Sell'] = trybenefict <= profitTable['Benefit']

        return profitTable
