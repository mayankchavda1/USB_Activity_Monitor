import logging
import csv
import os
from datetime import datetime

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

TXT_LOG = os.path.join(LOG_DIR, "activity_log.txt")
CSV_LOG = os.path.join(LOG_DIR, "activity_log.csv")

logging.basicConfig(
    filename=TXT_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(message)s"

)

def log_event(event,details):

    message = f"{event} | {details}"

    logging.info(message)

    print(message)

    with open(CSV_LOG, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            event,
            details
        ])