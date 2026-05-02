import requests
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")



OWN_POINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 12.971599
MY_LONG = 77.594566
api_key= os.environ.get("OWN_API_KEY")
params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    "appid": api_key,
    "cnt":4,

}


response = requests.get(OWN_POINT, params=params)
print(response.status_code)
weather_data=response.json()
print(weather_data)
# Access the first item in the 'weather' list, then the 'id'
# Use 'list' and index [0] for the first forecast entry
#weather_id = weather_data['list'][0]['weather'][0]['id']
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Carry an Umbrella,It's gonna rain!",
        from_="+19899004310",
        to="your_number",
    )
    print(message.status)






