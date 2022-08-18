import pymysql
import json

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
        sql = f'SELECT * FROM stock WHERE id = {id}'

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            print(datos)
        except Exception as e:
            raise

data = DataBase()
data.load_data()
