import logging
import os
import sys

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


logger.info("Loading Configurations...")
# Use python >=3.8
if sys.version_info[0] < 3 or sys.version_info[1] < 8:
    logger.error(
        "You MUST have a python version of at least 3.8! Multiple features depend on this. Bot quitting."
    )
    quit(1)

APP_ID = int(os.environ.get("APP_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
TOKEN = os.environ.get("TOKEN", "")
SESSION = os.environ.get("SESSION", "")
DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", 0))
OWNER_ID = int(os.environ.get("OWNER_ID", 0))