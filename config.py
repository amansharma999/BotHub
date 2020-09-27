from sample_config import Config

class Config(Config):
    #TG_BOT_TOKEN = "1365498867:AAHt3VWAHnG_PxMJgHpLgY4Uv4wdvNy8I2w"
    # These example values won't work. You must get your own app_id and
    # api_hash from https://my.telegram.org, under API Development.
     #APP_ID = 1108982
    #API_HASH = "babad37bef120d5c76a1fa02e3c2b5f5"
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = 1108982
    API_HASH = babad37bef120d5c76a1fa02e3c2b5f5
    # Photo Chat - Get this value from http://antiddos.systems
    API_TOKEN = "d6e8bf28-226c-420b-8baa-56ccb53f2db9"
    # Get this value from https://t.me/SitiSchu! Please do not steal, group for support https://t.me/SpamWatchSupport
    SPAMWATCH_API = "hAlogsz5yVFw4TYjIf6I993YFpZj~AT_5wCNrwnY3YeekgeEH1g62hO1hog02UHO"
    # Genius lyrics get this value from https://genius.com/developers both has same values
    GENIUS_API_TOKEN = "z4p8vWsqfVGzPtFeIjZ3N_rVmhqIwfcMEdgr-RNsOMoztYLrjt23YXCBhqBuWenA"
    # Genius lyrics get this value from https://genius.com/developers both has same values
    GENIUS = "z4p8vWsqfVGzPtFeIjZ3N_rVmhqIwfcMEdgr-RNsOMoztYLrjt23YXCBhqBuWenA"
    # Default alive name for .on cmd
    ALIVE_NAME = "xcruzhd2"
    # Userbot logging feature switch.
    BOTLOG = True
    # PhotoChat - don't change this value from http://antiddos.systems
    API_URL = "http://antiddos.systems"
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    HU_STRING_SESSION = "1BVtsOH4BuyMOVOD4PNMqNQLuPhzRiJdW3D03OuiBSbQ42vbNAqRpa1nnGcA1QF3dOG4UWp-1HtGFeoCJZlt5VbtKVTOUsn1JerW18sadaJa8jOxb7HfSlSkvK0Vjf4TTMOpx8Cs3Lh5Kzj9wGs5hwHGii43U8S-6xJjyHCA0JLbF2dcPGA8hRNyp6-Je0HKUeyYjaeY7sk6SFibwwW1BpKZQc-lRF6gxCqfdoVrzRQuhX1TlmwrsX5xGfjplAg1PmUZJ05kx9xUYsEziqsFe0h6U-3yTziMMWrdemagd-f5U5t4zfbbJTcX6Gj0q1zcssbRh7B21-MY6Txld3SYu9kaKnpFusQA="
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = "9d23649c66852b6b3838138bd5e7b571"
    # Your City
    WEATHER_DEFCITY = "sheopur"
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    #SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = -417001223
    # Send .get_id in any channel to fill this value. ReQuired for @Manuel15 inspiration to work!
    PRIVATE_CHANNEL_BOT_API_ID = -1001436635545
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
   # IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    #IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # This is required for the hash to torrent file functionality to work.
    #HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = "@xcruzhd2"
    # Get a Free API Key from OCR.Space
    #OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = -417001223
    # TG API limit. An album can have atmost 10 media!
    TG_GLOBAL_ALBUM_LIMIT = 9
    # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = "1365498867:AAHt3VWAHnG_PxMJgHpLgY4Uv4wdvNy8I2w"
    TG_BOT_USER_NAME_BF_HER = "@xcruzxbot"
    #
    #
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want userbot's features
    #UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None,
        view_messages=None,
        send_messages=True
    )
    # chat ids or usernames, it is recommended to use chat ids,
    # providing usernames means an additional overhead for the user
   # CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    # specify LOAD and NO_LOAD
    #LOAD = []
    # foloowing plugins won't work on Heroku,
    # ⚡Remove This To Make Them Work But Would Make Bot Unstable AF...⚡
    #NO_LOAD = [
                    
           #         "left",
        #            "autores",
      #              "hand",   
                    
   # ]
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = "TZ2e5YStFqGYQEUQhiyXAW6q"
    # you can set any name here
    SLAP_USERNAME = xcruzhd2
    # Get this from Github
    GITHUB_ACCESS_TOKEN = "7af24488fbe9336ffa147b849fb160a502ec4535"
    GIT_REPO_NAME = "amansharma999/BotHub"
    # Set to True if you want to block users that are spamming your PMs.
    NO_P_M_SPAM = True
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = 3
    # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NC_LOG_P_M_S = False
    # send .get_id in any channel to forward all your NEW PMs to this group
    PM_LOGGR_BOT_API_ID = -1001436635545
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    #DB_URI = os.environ.get("DATABASE_URL", None)
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    #MONGO_URI = os.environ.get("MONGO_URI", None)
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = 10
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = "\."
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    #SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    # VeryStream only supports video formats
   # VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
   # VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    # for temporary saving files on UserBot
    TEMP_DIR =  None
    # This is required for few things
    CHANNEL_ID = "-1001436635545"
    # Google Drive ()
    G_DRIVE_CLIENT_ID = None
    G_DRIVE_CLIENT_SECRET = None
    GDRIVE_FOLDER_ID = None
    AUTH_TOKEN_DATA =  None
    os.makedirs(TMP_DOWNLOAD_DIRECTORY, exist_ok=True)
    t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
    t_file.write(AUTH_TOKEN_DATA)
    t_file.close()
    #
    TELE_GRAM_2FA_CODE = None
    #
    #GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
    # rapidleech plugins
    # don't change the values
    OPEN_LOAD_LOGIN = "100"
    OPEN_LOAD_KEY =  "100"
    # Google Chrome Selenium Stuff
    # taken from https://github.com/jaskaranSM/UniBorg/blob/9072e3580cc6c98d46f30e41edbe73ffc9d850d3/sample_config.py#L104-L106
    GOOGLE_CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
    GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    # Chrome Driver and Headless Google Chrome Binaries
    CARBON_DRIVER = "/usr/bin/chromedriver"
    CARBON_BIN = "/usr/bin/chromium-browser"
    # get your value from https://Intellivoid.info
    LYDIA_API = "58247fff9e180eebfc073d8965dfd96f393ae00b9fa120255fb023bf3f9f78de088d28f4e3814feaf3e82be82515574e98573edf2654ec43cb910c1110ebdb9e"
    LYDIA_ANTI_PM = True
    # get your value from YouTube or Google.
    YOUTUBE_API_KEY = None
    # Heroku API_Key is found under "dashboard.heroku.com/account"
    HEROKU_MEMEZ = False
    HEROKU_API_KEY = "1f0ffcb0-4567-4275-89b9-976c76b10e8a"
    HEROKU_APP_NAME = None
    # required for Carbor
    CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
    CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    # define "repo_link" in conig_vars
    REPO_LINK = "https://github.com/amansharma999/BotHub.git"
    # define "UPSTREAM_REPO_URL" in conig_vars
    UPSTREAM_REPO_URL = "https://github.com/mkaraniya/BotHub.git"
    # define "HEROKU_GIT_URL" | https://git.heroku.com/YOUR_HEROKU_APP_NAME.git
    HEROKU_GIT_URL = "https://github.com/amansharma999/BotHub.git"
    # define "heroku_link" in conig_vars 
    HEROKU_LINK = "https://github.com/amansharma999/BotHub.gi"
    # define "packs_content" in conig_vars
    PACKS_CONTENT = None
    #
    BOT_HUB = None
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True

    
# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
admin_cmd = {}
USER_afkb = False
AFKBREASON = None
reason = None
    #
    
  