import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Environment:
    def __init__(self):
        self.host = os.environ.get("HOST")
        self.auth_url = os.environ.get("AUTH_URL")
        self.post_data = os.environ.get("POST_DATA")
        self.post_data_anyone = os.environ.get("POST_DATA_ANYONE")
        self.folder_path = os.environ.get("FOLDER_PATH")
        self.host_inhub = os.environ.get("HOST_INHUB")
        self.auth_url_inhub = os.environ.get("AUTH_URL_INHUB")
        self.get_data_inhub = os.environ.get("GET_DATA_INHUB")
        self.auth = {
            "loginApi": {"email": os.environ.get("API_LOGIN"), "password": os.environ.get("API_PASSWORD")},
        }
        self.auth_inhub = {
            "loginInhub": {"user_name": os.environ.get("INHUB_LOGIN"), "password": os.environ.get("INHUB_PASSWORD")},
        }