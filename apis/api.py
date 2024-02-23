import requests

# Get request 
response = requests.get('https://www.mapquestapi.com/directions/v2/route?key=47WpsLDQHmWJWawsQQdjNujjszN7xLee&from=Clarendon%20Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA')

print(response.status_code)

print(response.json())