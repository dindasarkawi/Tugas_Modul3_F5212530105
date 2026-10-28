from models.anggota_model import AnggotaModel

model = AnggotaModel()

print("=== PENGUJIAN CREATE & READ ANGGOTA ===")

# 1. Menguji fungsi Create (menambah anggota baru)
# Hapus tanda komentar (#) pada 3 baris di bawah ini jika ingin menambah data baru
print("\n[-] Menambahkan data anggota...")
model.create_anggota("Fatan Mohammad", "Jl. Merpati, Palu")
model.create_anggota("Budi Santoso", "Jl. Rajawali No. 15")

# 2. Menguji fungsi Read (menampilkan data anggota)
print("\n=== Daftar Anggota Perpustakaan ===")
daftar_anggota = model.get_all_anggota()

if len(daftar_anggota) > 0:
    for anggota in daftar_anggota:
        print(
            f"[{anggota['id_anggota']}] "
            f"Nama: {anggota['nama']} | "
            f"Alamat: {anggota['alamat']}"
        )
else:
    print("Belum ada data anggota.")