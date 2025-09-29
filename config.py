from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database config
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# NSE URLs
NSE_BASE_URL = os.getenv("NSE_BASE_URL")
NSE_NIFTY50_URL = os.getenv("NSE_NIFTY50_URL")

# Request Headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}


# Mail config
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_TO_ADDRESS = os.getenv("MAIL_TO_ADDRESS").split(",")
MAIL_CC_ADDRESS = os.getenv("MAIL_CC_ADDRESS").split(",")

# Debug print (remove in prod)
print("DB Config:", DB_USER, DB_HOST, DB_NAME)
print("NSE API URL:", NSE_NIFTY50_URL)
print("Mail To:", MAIL_TO_ADDRESS)
