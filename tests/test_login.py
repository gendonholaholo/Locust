from locust import HttpUser, task, between
from config import config
from utils.json_handler import load_user_data
from utils.logger import log_request

import random

class LoginTest(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def login_staging_bo(self):
        """Stress test endpoint login di Staging BO berdasarkan data dari idpass.json"""
        users = load_user_data()
        if not users or len(users) == 0:  # Pastikan user list tidak kosong
            print("⚠️ Tidak ada user untuk login.")
            return

        user = random.choice(users)
        payload = {"email": user["email"], "password": user["password"]}

        response = self.client.post(
            f"{config.STAGING_BO_URL}{config.ENDPOINTS_STAGING_BO['login']}",
            headers=config.HEADERS_STAGING_BO,
            json=payload
        )

        log_request("Login", response)

        if response.status_code == 200:
            print(f"✅ Login berhasil untuk {payload['email']}.")
        else:
            print(f"❌ Gagal login untuk {payload['email']}. Status kode: {response.status_code}, Respons: {response.text}")
