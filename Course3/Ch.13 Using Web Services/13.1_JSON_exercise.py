''' Exercise 1:
Change either geojson.py or geoxml.py to print out the two character country code from the
retrieved data. Add error checking so your program does not traceback if the country code
is not there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle
locations that are not in any country
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("Enter Q to quit OR")
    address = input('Enter location: ')
    if len(address) < 1 or address == 'Q' or address == 'q':
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # [-1] to get the last element
    address_com = js["results"][0]["address_components"]
    if len(address_com) >= 2:
        countryCode = address_com[-1]["short_name"]
        print(f"Country Code: {countryCode}")
    else:
        countryCode = address_com[0]["short_name"]
        print(f"There is no Country Code for {address}")

    # print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)
