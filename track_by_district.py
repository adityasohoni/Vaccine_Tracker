import requests
import time
import os
from datetime import date, datetime

# STEPS TO FOLLOW
# Go to this this url👇 in a browser to get your state ID
# https://cdn-api.co-vin.in/api/v2/admin/location/states
# Go to this this url👇 in a browser to get your district ID by replacing {state_id} with your state ID
# https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}
# Finally get your district ID and assign it to the variable district_id below
district_id = '___'
# Check the vaccine and age configuration at line 44
# Save and Run the script!
# Keep the script running till you find a vaccine
# When you hear the notification head over to the COWIN app/webpage and book your vaccine!


def alert(name):
    os.system('spd-say "The vaccine is available at {}"'.format(name))


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 "
                         "Safari/537.36"}
flag = 0
while True:
    if flag == 0:
        time.sleep(3.4)
    date_var = date.today().strftime("%d-%m-%Y")

    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date_var

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
            # Uncomment one of the two lines below if you are looking for a specific vaccine
            # if session['vaccine'] == 'COVAXIN':
            # if session['vaccine'] == 'COVISHIELD':
                if session['available_capacity'] > 0:
                    # Uncomment the below line if you are below 45 years of age
                    # if session['min_age_limit'] == 18:
                        alert(center['name'])
                        print(center['name'])
                        print(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        time.sleep(3.4)
                        print(session)
                        flag = 1

    if flag == 0:
        print("Not available at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
