from utils import Utils
from scraping import FinViz_scraper

if __name__ == '__main__':
    utils = Utils()

    utils.read_companies('Data/companies.csv')
    scraper = FinViz_scraper()
    compData = scraper.get_value()
    print(compData)
