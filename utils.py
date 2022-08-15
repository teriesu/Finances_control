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

        compActData['ActValue'] = compActData['ActValue'].astype(float)
        newInvest =  compData['StartInvest'] * compActData['ActValue'] / compData['StartValue']
        benefit = newInvest - compData['StartInvest']
        trybenefict = compData['StartInvest']*benefitIntent
        sellCriterium = trybenefict <= benefit
        percentbenefit = (100*newInvest/compData['StartInvest'])-100

        profitTable = pd.DataFrame()
        profitTable['Action'] = compData['Name']
        profitTable['CompID'] = compActData['CompID']
        profitTable['StartInvest'] = compData['StartInvest']
        profitTable['ActInvest'] = newInvest
        profitTable['Benefit'] = benefit
        profitTable['percent'] = percentbenefit
        profitTable['Sell'] = sellCriterium

        return profitTable
