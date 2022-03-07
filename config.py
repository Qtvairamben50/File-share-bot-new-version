import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝐻𝑒𝑙𝑙𝑜𝑜𝑜𝑜...😉{first}\n\n𝐼 𝑐𝑎𝑛 𝑠𝑡𝑜𝑟𝑒 𝑝𝑟𝑖𝑣𝑎𝑡𝑒 𝑓𝑖𝑙𝑒𝑠 𝑖𝑛 𝑆𝑝𝑒𝑐𝑖𝑓𝑖𝑒𝑑 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 𝑎𝑛𝑑 𝑜𝑡ℎ𝑒𝑟 𝑢𝑠𝑒𝑟𝑠 𝑐𝑎𝑛 𝑎𝑐𝑐𝑒𝑠𝑠 𝑖𝑡 𝑓𝑟𝑜𝑚 𝑠𝑝𝑒𝑐𝑖𝑎𝑙 𝑙𝑖𝑛𝑘.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐻𝑒𝑙𝑙𝑜𝑜𝑜𝑜...😉{first}\n\n<b>𝑌𝑜𝑢 𝑛𝑒𝑒𝑑 𝑡𝑜 𝑗𝑜𝑖𝑛 𝑚𝑦 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 /𝑔𝑟𝑜𝑢𝑝 𝑎𝑛𝑑 𝑢𝑠𝑒 𝑚𝑒.. ☺️\n\n𝑃𝑙𝑒𝑎𝑠𝑒 𝑗𝑜𝑖𝑛 𝑚𝑒 𝑚𝑦 𝑐ℎ𝑎𝑛𝑛𝑒𝑙🤪</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
