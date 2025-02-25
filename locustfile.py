from locust import HttpUser, task, between
from config import config, proxy_handler, wait_time
from tests.test_register import RegisterTest
from tests.test_login import LoginTest

import json
import os
import random
import string

class UserBehavior(HttpUser):
    wait_time = wait_time.gaussian_wait_time

    @task(10)
    def register_test(self):
        """Menjalankan register lebih cepat sebelum login"""
        RegisterTest.register_staging_bo(self)

    @task(5)
    def login_test(self):
        """Login hanya berjalan jika idpass.json sudah berisi user"""
        if os.path.exists("utils/idpass.json") and os.stat("utils/idpass.json").st_size > 0:
            LoginTest.login_staging_bo(self)
        else:
            print("⚠️ Tidak ada user terdaftar, menunggu register selesai...")
