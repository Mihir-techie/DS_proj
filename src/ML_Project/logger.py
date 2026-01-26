import logging
import os
from datetime import datetime

# 1️⃣ Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 2️⃣ Create log file name (NO folders here)
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# 3️⃣ Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# 4️⃣ Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
