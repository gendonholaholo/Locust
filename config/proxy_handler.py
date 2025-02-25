import random

PROXY_LIST = [
    "172.232.236.34:1080",
    "103.184.67.37:1080",
    "103.217.224.129:1080",
    "180.250.91.50:5678",
    "103.10.99.110:5678",
]

def get_random_proxy():
    """Mengambil proxy secara acak dari daftar atau mengembalikan None jika kosong"""
    if not PROXY_LIST:
        return None  # Pastikan tidak mengembalikan dict kosong

    proxy = random.choice(PROXY_LIST)
    return {"http": f"http://{proxy}", "https": f"https://{proxy}"}
