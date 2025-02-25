from config import config
from utils.json_handler import save_user_data
from utils.logger import log_request
from locust import HttpUser, task, between

import random
import string
import os
import json

class RegisterTest(HttpUser):
    wait_time = between(1, 3)

    def random_string(self, length=10):
        """Membuat string random untuk email & password"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    @task(5)
    def register_staging_bo(self):
        """Stress test endpoint register di Staging BO & simpan ke idpass.json"""
        random_email = f"{self.random_string()}@test.com"
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

        log_request("Register", response)

        if response.status_code == 201:
            print(f"User {random_email} berhasil register di Staging BO.")
            save_user_data(random_email, password)  # Gunakan handler JSON modular
