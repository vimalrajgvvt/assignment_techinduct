import logging
import sys

# [cite_start]Structured logging setup [cite: 16]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger("Address_Book_API")