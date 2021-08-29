import os
from dotenv import load_dotenv


load_dotenv()


SODAPY_APPTOKEN = os.getenv('SODAPY_APPTOKEN')
SODAPY_DOMAIN = os.getenv('SODAPY_DOMAIN')
SODAPY_DATASET_IDENTIFIER = os.getenv('SODAPY_DATASET_IDENTIFIER')
GOOGLE_ENDPOINT = os.getenv('GOOGLE_ENDPOINT')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
