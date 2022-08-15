from utils import Utils
from scraping import FinViz_scraper

if __name__ == '__main__':
    utils = Utils()
    scraper = FinViz_scraper()

    compData = utils.read_companies()
    compActData = scraper.get_value()

    print(utils.calcProffit(compData, compActData))
