import psycopg2
from configparser import ConfigParser
from userdata.UserData import UserData

class UserDataSupplier:

    def __init__(self):
        self.db_config = self.config()

    def get_user_data(self, login, password):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT first_name, second_name FROM user_info WHERE login='{0}' and password = '{1}';".format(login, password))
        result = cur.fetchone()
        conn.close()
        if result:
            return tuple([UserData(result[0], result[1]), ""])
        else:
            return tuple([None, "Логин или пароль не верен"])

    def get_connection(self):
        conn = psycopg2.connect(**self.db_config)
        return conn


    def config(self, filename = 'database.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
