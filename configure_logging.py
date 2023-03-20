import logging
import logging.handlers
import os
import sys
from dotenv import load_dotenv
load_dotenv()
sys.stdout.reconfigure(encoding='utf-8')

# configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_path = os.environ["LOGGING_PATH"]
formatter = logging.Formatter("%(asctime)s %(levelname).5s :: %(message)s")

# timed rotating handler to log to file at DEBUG level, rotate every 100 KB
debug_file_handler = logging.handlers.RotatingFileHandler(log_path + "debug.log", mode="a", maxBytes=100000, backupCount=1, encoding='utf-8', delay=False)
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(formatter)
logger.addHandler(debug_file_handler)

# log debug messages to sdout
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# handler to log to a different file at ERROR level, rotate every 100 KB
error_file_handler = logging.handlers.RotatingFileHandler(log_path + "error.log", mode="a", maxBytes=1000000, backupCount=10, encoding='utf-8', delay=False)
error_file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s %(levelname).5s :: %(message)s")
error_file_handler.setFormatter(formatter)
logger.addHandler(error_file_handler)