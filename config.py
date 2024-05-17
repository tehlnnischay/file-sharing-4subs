# https://t.me/blackworldbackup0



import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7068442783:AAH9zdA33dFiOI5ZUnMLCxlqxXaX0jhX8Vc")
APP_ID = int(os.environ.get("APP_ID", "27315697"))
API_HASH = os.environ.get("API_HASH", "dbc404a4c78480c09dd5d693fc13c1b8")


OWNER = os.environ.get("OWNER", "hellloska") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "6820525129")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://thor:7thor7@thor.aymqpdl.mongodb.net/?retryWrites=true&w=majority&appName=thor")
DB_NAME = os.environ.get("DB_NAME", "HDMEDIA03")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002141441410")) #database id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001935247305"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002113909424"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002067058871"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002144760143"))


SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

try:
    ADMINS=[5146039165]
    for x in (os.environ.get("ADMINS", "5146039165").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(6820525129)

LOG_FILE_NAME = "uxblogs.txt"

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
   





# https://t.me/ultroid_official
