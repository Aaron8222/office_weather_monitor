import requests
import time
from creds import API_KEY

URL = 'https://api.thingspeak.com/update'

def read_temperature():
    # Replace with your actual sensor code
    return 23.4

while True:
    temp = read_temperature()
    response = requests.get(URL, params={'api_key': API_KEY, 'field1': temp})
    print(f"Sent temperature: {temp}, Response: {response.text}")
    time.sleep(20)  # send every 15 seconds
