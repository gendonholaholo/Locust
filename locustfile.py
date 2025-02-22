from locust import HttpUser, task, between
import config
import random
import string

class UserBehavior(HttpUser):
    wait_time = between(1, 3)  # Simulasi delay antar request
    user_list = []  # Pindahkan daftar user ke dalam kelas

    def random_string(self, length=8):
        """Membuat string random untuk username dan password"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @task(2)
    def register(self):
        """Simulasi banyak user yang mendaftar di Staging dan menyimpan akun ke daftar user_list"""
        username = self.random_string()
        password = self.random_string()

        payload = {
            "username": username,
            "password": password
        }
        response = self.client.post(
            f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['register']}",
            headers=config.HEADERS_STAGING,
            json=payload
        )

        if response.status_code == 201:  # Jika berhasil register, simpan user ke daftar
            self.user_list.append({"username": username, "password": password})
            print(f"User {username} berhasil terdaftar.")
        else:
            print(f"Gagal register user {username}. Status kode: {response.status_code}")

    @task(3)
    def login(self):
        """Simulasi banyak user login dengan akun yang berbeda"""
        if not self.user_list:  # Cek apakah ada user yang tersedia
            return

        user = random.choice(self.user_list)  # Pilih user secara acak untuk login

        payload = {
            "username": user["username"],
            "password": user["password"]
        }

        response = self.client.post(
            f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['login']}",
            headers=config.HEADERS_STAGING,
            json=payload
        )

        if response.status_code == 200:
            print(f"User {user['username']} berhasil login.")
        else:
            print(f"Gagal login untuk {user['username']}. Status kode: {response.status_code}")

    @task(1)
    def create_session_waha(self):
        """Mengukur kecepatan pembuatan session di WAHA API"""

        # Menambahkan nama sesi unik untuk setiap request
        session_name = f"session_{self.random_string(8)}"

        payload = {
            "name": session_name,  # Nama sesi
            "config": {
                "debug": True  # Menyalakan mode debug (sesuai dokumentasi WAHA)
            }
        }

        try:
            response = self.client.post(
                f"{config.API_BASE_URL_WAHA}{config.ENDPOINTS_WAHA['create_session']}",
                headers=config.HEADERS_WAHA,
                json=payload
            )

            if response.status_code == 201:
                print(f"Sesi {session_name} berhasil dibuat.")
            else:
                print(f"Gagal membuat sesi {session_name}. Status kode: {response.status_code}, Respons: {response.text}")

        except Exception as e:
            print(f"Terjadi error saat membuat sesi WAHA: {str(e)}")

    @task(1)
    def test_landing_page(self):
        """Mengukur kecepatan akses landing page di Staging"""
        response = self.client.get(
            f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['landing_page']}"
        )

        if response.status_code == 200:
            print("Landing page berhasil diakses.")
        else:
            print(f"Gagal mengakses landing page. Status kode: {response.status_code}")
