import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "21159773")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "49ae08543a07335e195756eba2f56e11") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6710510477:AAE3YFDMHWT3d6prygYFzlc285OmpQPpZB0") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else [] #Keep thia empty otherwise bot will not work for owner.
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Greylinks")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aaroha:aaroha@cluster0.xfupmjy.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "6959948002")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6959948002)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "2025097901")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "GreyMattersTech") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/19eeb26fa2ce58765917a.jpg') # image when someone hit /start
LINK_BYPASS = "True" 
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""
