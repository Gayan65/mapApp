import urllib.parse
import requests

# Api Call for direction
def get_direction(orig, dest):
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "47WpsLDQHmWJWawsQQdjNujjszN7xLee"
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    return json_data