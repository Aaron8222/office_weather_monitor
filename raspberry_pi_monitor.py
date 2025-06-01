import requests
import time
from creds import API_KEY
import os
import glob


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

URL = 'https://api.thingspeak.com/update'

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temperature():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_c = float(lines[1][equals_pos + 2:]) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32
        return temp_f

while True:
    temp = read_temperature()
    response = requests.get(URL, params={'api_key': API_KEY, 'field1': temp})
    print(f"Sent temperature: {temp}, Response: {response.text}")
    time.sleep(20)  # send every 20 seconds
