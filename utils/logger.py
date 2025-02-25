import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "locust_test.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)


logging.getLogger().addHandler(console_handler)

def log_request(api_name, response):
    """Mencatat status kode dan response API ke dalam log file"""
    if response is None:
        logging.error(f"[{api_name}] ❌ Request gagal: Tidak ada response")
        return

    if response.status_code >= 400:
        logging.error(f"[{api_name}] ❌ Error {response.status_code}: {response.text}")
    else:
        logging.info(f"[{api_name}] ✅ Status: {response.status_code}, Response: {response.text}")
