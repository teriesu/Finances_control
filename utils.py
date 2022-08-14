import pandas as pd

class Utils:

    def read_companies(self, path, columns = None):
        companies = pd.read_csv('Data/companies.csv')
        if columns is None:
            return companies
        else:
            compCol= companies[columns]
            return compCol

    def calcProffit(self, compData, compActData):
        compActData['ActValue'] = compActData['ActValue'].astype(float)
        newInvest =  compData['StartInvest'] * compActData['ActValue'] / compData['StartValue']
        benefit = newInvest - compData['StartInvest']
        print(benefit)
        print(newInvest)
