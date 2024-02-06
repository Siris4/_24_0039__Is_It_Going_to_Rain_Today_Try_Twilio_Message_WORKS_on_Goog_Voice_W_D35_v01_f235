import os
import requests
from twilio.rest import Client

# environment variable master string:

# extracting sensitive data from environment variables:
API_KEY = os.environ.get('API_KEY', 'API_KEY does not exist')
ACCOUNT_SID = os.environ.get('ACCOUNT_SID', 'ACCOUNT_SID does not exist')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN', 'AUTH_TOKEN does not exist')

# print statements to check the values:
print(f"The API_KEY is: {API_KEY}")
print(f"The ACCOUNT_SID is: {ACCOUNT_SID}")
print(f"The AUTH_TOKEN is: {AUTH_TOKEN}")

# weather api endpoint and parameters:
API_Weather_URL_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
lat, lon = 31.332939, -94.727882  # coordinates for Lufkin, TX
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "cnt": 4,
}

# make api request and process response:
response = requests.get(url=API_Weather_URL_Endpoint, params=weather_params)
response.raise_for_status()  # raise an exception for http errors:
data = response.json()
print(f"The JSON data is: {data}")

# check for rain in the forecast:
will_rain = any(int(hour_data["weather"][0]["id"]) < 600 for hour_data in data["list"])
if will_rain:
    print("Bring an umbrella!")
    # twilio client setup and sending sms:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain. Bring an umbrella!",
        from_="+18888462616",  # your Twilio number (replace if different)
        to='+17654189611'  # your personal cell phone number
    )
    print("SMS sent!")


    #IF SMS WORKING, DISABLE BELOW HERE:


    # subject = f"Subject: Your 12 Hour heads up of precipitation!!!\n\n"  # {birthday_person.name}
    # body = "It's going to rain within 12 hours here. Bring an umbrella!"
    # email_being_sent_to2 = "test1.omega1000@gmail.com"
    #
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email1, password=my_email_app_password)
    #     connection.sendmail(
    #         from_addr=my_email1,
    #         to_addrs=email_being_sent_to2,
    #         msg=f"{subject}{body}"
    #     )

