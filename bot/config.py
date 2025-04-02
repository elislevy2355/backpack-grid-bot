import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.secret_key = os.getenv("SECRET_KEY")
        self.base_url = "https://api.backpack.exchange"
