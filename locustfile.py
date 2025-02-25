from locust import HttpUser, task, between
from config import config, proxy_handler, wait_time
from tests.test_register import RegisterTest
from tests.test_login import LoginTest
from utils.logger import log_request
from config.wait_time import WaitTime

import json
import os
import random
import string

class UserBehavior(HttpUser):
    wait_time = WaitTime.gaussian_wait_time

    @task(10)
    def register_test(self):
        """Menjalankan register lebih cepat sebelum login"""
        register_instance = RegisterTest(self.environment)  # Buat instance dari RegisterTest
        random_email = f"{register_instance.random_string()}@test.com"  # Panggil method dengan benar
        print(f"📩 Email yang dibuat: {random_email}")

        response = register_instance.register_staging_bo()  # Gunakan instance untuk panggil method
        if response is not None:
            log_request("Register Task", response)
        else:
            print("⚠️ Register gagal, tidak ada response.")

    @task(5)
    def login_test(self):
        """Login hanya berjalan jika idpass.json sudah berisi user"""
        if os.path.exists("utils/idpass.json") and os.stat("utils/idpass.json").st_size > 0:
            response = LoginTest.login_staging_bo(self)

            if response is not None:
                log_request("Login Task", response)
            else:
                print("⚠️ Login gagal, tidak ada response.")
        else:
            print("⚠️ Tidak ada user terdaftar, menunggu register selesai...")
