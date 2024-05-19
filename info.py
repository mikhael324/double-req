import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '4052973'))
API_HASH = environ.get('API_HASH', '3238bd8ae26df065d11c4054fe8a231c')
BOT_TOKEN = environ.get('BOT_TOKEN', '7117213451:AAGYWPTQTEHFeha6jpeLTsmv977jhOBVrHM')
PORT = environ.get("PORT", "8080")
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/39204c3e376d9a367717e.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/253e5f006ba6a7ea4c232.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/ad240f9e93fb7c08be841.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/253e5f006ba6a7ea4c232.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '707282066').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001761183308 -1001702551529 -1001227981388 -1001738644907 -1001794047221').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001553475113')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL_1 = environ.get("REQ_CHANNEL_1", "-1002117004229")
REQ_CHANNEL_1 = int(REQ_CHANNEL_1) if REQ_CHANNEL_1 and id_pattern.search(REQ_CHANNEL_1) else None

REQ_CHANNEL_2 = environ.get("REQ_CHANNEL_2", "-1002048602510")
REQ_CHANNEL_2 = int(REQ_CHANNEL_2) if REQ_CHANNEL_2 and id_pattern.search(REQ_CHANNEL_2) else None

auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
DELETE_TIMEOUT = int(environ.get('DELETE_TIMEOUT', 30)) # 2 hours in seconds
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://plotlinethe:fe1q1QrgZKRCv6aM@cluster0.muggrce.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_Files')
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://https://t.me/+AngJ8lGmH4wwNWY1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/ccl_links')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001716429576'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'ccl_links')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>File Name:</b> <code>{file_name}</code> \n \n \n <b>🔰👉 Subscribe our Youtube Channel to win free Iphone Giveaway🥺👇 ❤️  \n \n https://youtube.com/@ThePlotlinee \n https://youtube.com/@ThePlotlinee \n https://youtube.com/@ThePlotlinee  \n \n ------------------------- \n ➧@Cinemaclub_3 \n ➧@Cinemaclub_4 \n ➧@ccl_links</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


## EXTRA FEATURES ##

      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'onepagelink.in')

URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '2a04850c9134367a527f536eb1807714f9290356')

     # Auto Delete For Group Message (Self Delete) #

SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 40))

SELF_DELETE = environ.get('SELF_DELETE', True)

if SELF_DELETE == "True":

    SELF_DELETE = True

    # Download Tutorial Button #

DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"

DOWNLOAD_TEXT_URL = "https://t.me/MvMKnowHow/5"

   # Custom Caption Under Button #

CAPTION_BUTTON = "Suscribe"

CAPTION_BUTTON_URL = "https://youtube.com/channel/UCqts9WhhlioK3RB9XQQzoAg"

   # Auto Delete For Bot Sending Files #
