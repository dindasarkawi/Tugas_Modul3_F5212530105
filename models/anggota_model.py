from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    # Menambahkan data anggota (Create)
    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                INSERT INTO {self.table_name} 
                (nama, alamat) 
                VALUES (%s, %s)
            """
            val = (nama, alamat)
            
            try:
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error saat menambah anggota: {e}")
                self.conn.rollback()
                return False
        return False

    # Menampilkan semua data anggota (Read)
    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            
            result = cursor.fetchall()
            cursor.close()
            return result
        return []