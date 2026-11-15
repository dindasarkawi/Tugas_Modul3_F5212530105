from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    # Menampilkan semua data buku
    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)

            result = cursor.fetchall()

            cursor.close()
            return result
        
        return []
    
    # Menambahkan data buku
    def create_buku(self, judul_buku, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name}
                (judul_buku, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """

            val = (judul_buku, penulis, tahun_terbit)

            cursor.execute(query, val)
            self.conn.commit()

            cursor.close()
            return True
        return False
    # Menambahkan/Mengubah data buku
    def update_buku(self, id_buku, judul_buku, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                UPDATE {self.table_name}
                SET judul_buku = %s, penulis = %s, tahun_terbit = %s
                WHERE id_buku = %s
            """
            val = (judul_buku, penulis, tahun_terbit, id_buku)
            try:
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error saat update: {e}")
                self.conn.rollback()
                return False
        return False
    # Menghapus data buku
    def delete_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id_buku = %s"
            val = (id_buku,)
            try:
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error saat delete: {e}")
                self.conn.rollback()
                return False
        return False