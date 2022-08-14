from utils import Utils
from scraping import FinViz_scraper

if __name__ == '__main__':
    utils = Utils()
    scraper = FinViz_scraper()

    compData = utils.read_companies('Data/companies.csv')
    compActData = scraper.get_value()

    utils.calcProffit(compData, compActData)
