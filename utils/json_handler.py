import json
import os

FILE_PATH = "utils/idpass.json"

def save_user_data(email, password):
    """Menyimpan data user ke dalam JSON."""
    user_data = {"email": email, "password": password}

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(user_data)

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_user_data():
    """Membaca data user dari idpass.json dengan validasi"""
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        print("❌ File idpass.json kosong atau tidak ditemukan.")
        return []

    try:
        with open(FILE_PATH, "r") as file:
            users = json.load(file)
        if not users:
            print("❌ Tidak ada user yang tersimpan di idpass.json.")
            return []
        return users
    except json.JSONDecodeError:
        print("❌ File idpass.json tidak bisa dibaca! Mungkin corrupt.")
        return []
