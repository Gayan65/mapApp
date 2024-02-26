import os
import urllib.parse
import requests
from dotenv import load_dotenv

load_dotenv()

# Api Call for direction
def get_direction(orig, dest):
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = os.getenv("KEY")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    return json_data