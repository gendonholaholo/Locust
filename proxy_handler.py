import random

PROXY_LIST = [
    "172.232.236.34:1080",
    "103.184.67.37:1080",
    "103.217.224.129:1080",
    "180.250.91.50:5678",
    "103.10.99.110:5678",
]

def get_random_proxy():
    if not PROXY_LIST:
        return None

    proxy = random.choice(PROXY_LIST)
    return {"http": proxy, "https": proxy}
