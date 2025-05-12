import logging
import os

import consts as c


os.makedirs(c.LOG_DIR, exist_ok=True)

logger = logging.getLogger("notifier")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(c.LOG_FORMAT, c.LOG_DATE_FORMAT)

file_handler = logging.FileHandler(
    os.path.join(c.LOG_DIR, c.LOG_FILE),
    encoding=c.LOG_ENCODING
)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
