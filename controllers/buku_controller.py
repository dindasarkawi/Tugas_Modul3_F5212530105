import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

# ARDHITA AMARLI PUTRI F5212530109
class BukuController:
    def __init__(self, user_role="anggota", on_logout=None):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView(role=self.user_role, on_logout=on_logout)

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_buku)
        self.view.btn_update.configure(command=self.update_buku)

        # Admin: klik baris di tabel otomatis mengisi form agar mudah di-update
        if self.user_role == "admin":
            self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_baris)

        self.muat_data_tabel()

    def _cek_admin(self, aksi):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                f"Anda tidak memiliki izin untuk {aksi} data!"
            )
            return False
        return True

    def _kosongkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    def isi_form_dari_baris(self, event=None):
        selected = self.view.tabel.focus()
        if not selected:
            return

        _, judul, penulis, tahun = self.view.tabel.item(selected, "values")

        self._kosongkan_form()
        self.view.entry_judul.insert(0, judul)
        self.view.entry_penulis.insert(0, penulis)
        self.view.entry_tahun.insert(0, tahun)

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for buku in self.model.get_all_buku():
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul_buku"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        if not self._cek_admin("menambah"):
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_buku(self):
        if not self._cek_admin("menghapus"):
            return

        selected = self.view.tabel.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return

        id_buku = self.view.tabel.item(selected, "values")[0]

        if self.model.delete_buku(id_buku):
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal Menghapus",
                "Buku tidak dapat dihapus. Kemungkinan buku ini masih tercatat "
                "dalam data peminjaman."
            )

    def update_buku(self):
        if not self._cek_admin("memperbarui"):
            return

        selected = self.view.tabel.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin diperbarui!")
            return

        id_buku = self.view.tabel.item(selected, "values")[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()