import mysql.connector


class Database:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "perpustakaan"

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            return connection

        except mysql.connector.Error as err:
            print(f"Error koneksi database: {err}")
            return None