# importing the requests library
import requests
import time
import os
from datetime import date
from datetime import datetime
# api-endpoint
pincodes = ['560008', #Add a list of pins to track
            '560030',
            '560078',
            '560076',
            '560002',
            '560037',
            '560020',
            '560034',
            '560041',
            '560001',
            '560066',
            '560003',
            '560010',
            '560011',
            '560100']

date_var = date.today().strftime("%d-%m-%Y")


def alert(name):
    os.system('spd-say "The vaccine is available at {}"'.format(name))


# sending get request and saving the response as response object
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

while True:
    for pincode in pincodes:
        time.sleep(3.5)
        URL = "http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date_var
        try:
            r = requests.get(url=URL, headers=headers)
        except requests.ConnectionError:
            print("No Network at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            continue
        print(r.status_code)
        data = r.json()

        flag = 0

        for center in data['centers']:
            for session in center['sessions']:
                if session['available_capacity'] > 3 and session['min_age_limit'] < 45 and session['vaccine'] == 'COVAXIN':
                # if session['available_capacity'] > 0:
                    alert(center['name'])
                    print(center['name'])
                    time.sleep(4)
                    print(session)
                    flag = 1
        if flag == 0:
            print("Not available at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
