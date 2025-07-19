import os
import logging
from datetime import datetime

# 1. Create log directory inside current project
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# 2. Log file path
log_filename = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"
log_path = os.path.join(log_dir, log_filename)

# 3. Set up logging
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 4. Log something
logging.info("✅ Logging test message")
print(f"Log written to {log_path}")
