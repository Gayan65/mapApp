import urllib.parse
import requests

# Get request 
# response = requests.get('https://www.mapquestapi.com/directions/v2/route?key=47WpsLDQHmWJWawsQQdjNujjszN7xLee&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA')

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rambukkana"
dest = "Colombo"
key = "47WpsLDQHmWJWawsQQdjNujjszN7xLee"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")

elif json_status == 402:
    print("\n****************************************************************")
    print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
    print("****************************************************************\n")
else:
    print("\n************************************************************************")
    print("Status Code: " + str(json_status) + "; Refer to:")
    print("https://developer.mapquest.com/documentation/directions-api/status-codes")
    print("************************************************************************\n")