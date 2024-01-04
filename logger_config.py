# logger_config.py

import logging

def setup_logger():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    # You can also add other configurations here, such as setting log file, log level, etc.

    # If you want to configure logging for specific libraries, you can do it here
    # Example: logging.getLogger("httpx").setLevel(logging.WARNING)
