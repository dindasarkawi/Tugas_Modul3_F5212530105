from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
# (Diberi tanda komentar '#' agar tidak menambah data yang sama setiap kali file dijalankan)
# print("Menambahkan data buku...")
# model.create_buku(
#     "Pemrograman Python MVC",
#     "Guido van Rossum",
#     2023
# )
# print("Data berhasil disimpan ke Laragon MySQL!")

print("=== PENGUJIAN UPDATE & DELETE ===")

# 2. Menguji fungsi Update (mengubah data buku)
# Contoh: Mengubah tahun terbit pada buku ID 1 menjadi 1981
print("\n[-] Memproses Update...")
if model.update_buku(1, "Bumi Manusia", "Pramoedya Ananta Toer", 1981):
    print("Berhasil: Data buku ID 1 telah diperbarui!")
else:
    print("Gagal: Data buku ID 1 tidak ditemukan.")

# 3. Menguji fungsi Delete (menghapus data buku)
# Contoh: Menghapus buku Python MVC yang memiliki ID 5
print("\n[-] Memproses Delete...")
if model.delete_buku(5):
    print("Berhasil: Data buku ID 5 telah dihapus!")
else:
    print("Gagal: Data buku ID 5 tidak ditemukan (mungkin sudah terhapus sebelumnya).")

# 4. Menguji fungsi Read (menampilkan data terbaru setelah diubah & dihapus)
print("\n=== Daftar Buku Terbaru ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul_buku']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )
    