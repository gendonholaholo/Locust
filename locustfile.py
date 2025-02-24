from locust import HttpUser, task, between
import config
import random
import string
import json
import os
import proxy_handler

class UserBehavior(HttpUser):
    wait_time = between(7, 17)

    @task
    def test_proxy_request(self):
        proxy = proxy_handler.get_random_proxy()
        if proxy:
            response = self.client.get(
                "https://staging-bo.agencerdas.id/api",
                proxies=proxy
            )
        else:
            print("Tidak ada proxy yang tersedia, menggunakan koneksi langsung.")
            response = self.client.get("https://staging-bo.agencerdas.id/api")

    user_list = []

    def random_string(self, length=8):
        """Membuat string random untuk username dan password"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @task(5)
    def register_staging_bo(self):
        """Stress test endpoint register di Staging BO & simpan ke idpass.json"""
        random_email = f"{self.random_string(10)}@test.com"
        random_phone = f"08{random.randint(1000000000, 9999999999)}"
        password = "123123123"

        payload = {
            "name": "Test Akun",
            "email": random_email,
            "phone_number": random_phone,
            "password": password,
            "password_confirmation": password
        }

        response = self.client.post(
            f"{config.STAGING_BO_URL}{config.ENDPOINTS_STAGING_BO['register']}",
            headers=config.HEADERS_STAGING_BO,
            json=payload
        )

        if response.status_code == 201:
            print(f"User {random_email} berhasil register di Staging BO.")

            user_data = {"email": random_email, "password": password}

            if os.path.exists("idpass.json"):
                with open("idpass.json", "r") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            data.append(user_data)

            with open("idpass.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            print(f"Gagal register user {random_email}. Status kode: {response.status_code}, Respons: {response.text}")

    @task(5)
    def login_staging_bo(self):
        """Stress test endpoint login di Staging BO berdasarkan data dari idpass.json"""
        if not os.path.exists("idpass.json") or os.stat("idpass.json").st_size == 0:
            print("File idpass.json kosong atau tidak ditemukan, tidak bisa login.")
            return

        with open("idpass.json", "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                print("File idpass.json tidak bisa dibaca!")
                return

        if not users:
            print("Tidak ada user untuk login!")
            return

        user = random.choice(users)
        payload = {
            "email": user["email"],
            "password": user["password"]
        }

        response = self.client.post(
            f"{config.STAGING_BO_URL}{config.ENDPOINTS_STAGING_BO['login']}",
            headers=config.HEADERS_STAGING_BO,
            json=payload
        )

        if response.status_code == 200:
            print(f"Login berhasil untuk {payload['email']}.")
        else:
            print(f"Gagal login untuk {payload['email']}. Status kode: {response.status_code}, Respons: {response.text}")

    # @task(2)
    # def register(self):
    #     """Simulasi banyak user yang mendaftar di Staging dan menyimpan akun ke daftar user_list"""
    #     username = self.random_string()
    #     password = self.random_string()
    #
    #     payload = {
    #         "username": username,
    #         "password": password
    #     }
    #     response = self.client.post(
    #         f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['register']}",
    #         headers=config.HEADERS_STAGING,
    #         json=payload
    #     )
    #
    #     if response.status_code == 201:  # Jika berhasil register, simpan user ke daftar
    #         self.user_list.append({"username": username, "password": password})
    #         print(f"User {username} berhasil terdaftar.")
    #     else:
    #         print(f"Gagal register user {username}. Status kode: {response.status_code}")
    #
    # @task(3)
    # def login(self):
    #     """Simulasi banyak user login dengan akun yang berbeda"""
    #     if not self.user_list:  # Cek apakah ada user yang tersedia
    #         return
    #
    #     user = random.choice(self.user_list)  # Pilih user secara acak untuk login
    #
    #     payload = {
    #         "username": user["username"],
    #         "password": user["password"]
    #     }
    #
    #     response = self.client.post(
    #         f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['login']}",
    #         headers=config.HEADERS_STAGING,
    #         json=payload
    #     )
    #
    #     if response.status_code == 200:
    #         print(f"User {user['username']} berhasil login.")
    #     else:
    #         print(f"Gagal login untuk {user['username']}. Status kode: {response.status_code}")
    #
    # @task(1)
    # def create_session_waha(self):
    #     """Mengukur kecepatan pembuatan session di WAHA API"""
    #
    #     # Menambahkan nama sesi unik untuk setiap request
    #     session_name = f"session_{self.random_string(8)}"
    #
    #     payload = {
    #         "name": session_name,  # Nama sesi
    #         "config": {
    #             "debug": True  # Menyalakan mode debug (sesuai dokumentasi WAHA)
    #         }
    #     }
    #
    #     try:
    #         response = self.client.post(
    #             f"{config.API_BASE_URL_WAHA}{config.ENDPOINTS_WAHA['create_session']}",
    #             headers=config.HEADERS_WAHA,
    #             json=payload
    #         )
    #
    #         if response.status_code == 201:
    #             print(f"Sesi {session_name} berhasil dibuat.")
    #         else:
    #             print(f"Gagal membuat sesi {session_name}. Status kode: {response.status_code}, Respons: {response.text}")
    #
    #     except Exception as e:
    #         print(f"Terjadi error saat membuat sesi WAHA: {str(e)}")
    #
    # @task(1)
    # def test_landing_page(self):
    #     """Mengukur kecepatan akses landing page di Staging"""
    #     response = self.client.get(
    #         f"{config.STAGING_URL}{config.ENDPOINTS_STAGING['landing_page']}"
    #     )
    #
    #     if response.status_code == 200:
    #         print("Landing page berhasil diakses.")
    #     else:
    #         print(f"Gagal mengakses landing page. Status kode: {response.status_code}")
