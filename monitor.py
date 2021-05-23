#!/usr/bin/env python3
# importing the requests library
import requests
import sys
import os
from datetime import datetime
  
date = datetime.now().strftime("%d-/%m-/%Y")
# api-endpoint
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=209&date="+date
# URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=670&date="+date

HEAD = {
'Host': 'cdn-api.co-vin.in',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Origin': 'https://www.cowin.gov.in',
'Connection': 'keep-alive',
'Referer': 'https://www.cowin.gov.in/',
'TE': 'Trailers'
}
  
r = requests.get(URL, headers=HEAD)
  
# extracting data in json format
  
response = r.json()
for center in response['centers']:
    for session in center['sessions']:
        if session['min_age_limit'] <= 18 and session['available_capacity'] > 0:
            # if "dharampur" in center['name'].lower() or "dharampur" in center['address'].lower():
                # print(center['name']+","+center['address'])
                # print("Age:{}".format(session['min_age_limit']))
                # print("Date:{}".format(session['date']))
                # print("Capacity:{}".format(session['available_capacity']))
                msg = 'notify-send -u critical \'Check Vaccinations Now\' ' + datetime.now().strftime("%H:%M:%S")
                os.system(msg)
                print("VAX")
                sys.exit()

print("NA")


