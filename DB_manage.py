import pymysql
import json
from scraping import FinViz_scraper
from datetime import datetime

class DataBase:
    def __init__(self):

        f = open('BDacces.json')
        data = json.load(f)

        self.connection = pymysql.connect(
        host = data['server'],
        user = data['username'],
        password = data['password'],
        db = data['database']
        )

        self.cursor = self.connection.cursor()

    def load_data(self):
        sql = 'SELECT * FROM stock'

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            print(datos)

        except Exception as e:
            raise

    def load_one_company(self, id):
        sql = f'SELECT * FROM stock WHERE CompID = {id}'

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            print(datos)
        except Exception as e:
            raise

    def del_invest(self, id):
        sql = f'DELETE FROM stock WHERE (CompID = {id});'

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            print(datos)

        except Exception as e:
            raise

    def create_invest(self, id, name, StartInvest):
        scraper = FinViz_scraper()

        sql = f"INSERT INTO stock (CompID, Name, StartValue, StartInvest, buyDate) VALUES ('{id}', '{name}', {scraper.actValue(id)}, {StartInvest}, '{datetime.today().strftime('%Y-%m-%d')}');"

        print(sql)
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            print(datos)

        except Exception as e:
            return e

data = DataBase()
data.create_invest('NVDA', 'NVIDIA Corporation', 20)
