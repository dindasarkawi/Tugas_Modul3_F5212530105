import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        user = self.model.autentikasi(username, password)

        if user:
            # Samakan format role agar pengecekan "admin"/"anggota" tidak meleset
            # karena huruf besar atau spasi di database
            role = str(user['role']).strip().lower()

            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']} ({role})!")
            # Tutup jendela Login
            self.view.destroy()
            # Buka jendela Utama Perpustakaan, kirim role dan fungsi untuk kembali ke login
            app_utama = BukuController(user_role=role, on_logout=self.kembali_ke_login)
            app_utama.run()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def kembali_ke_login(self):
        """Dipanggil BukuView setelah Logout: tampilkan lagi jendela Login yang baru."""
        AuthController().run()

    def run(self):
        self.view.mainloop()