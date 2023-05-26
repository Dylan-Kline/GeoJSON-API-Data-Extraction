""" 
Calling a JSON API In this assignment you will write a Python program
somewhat similar to http://www.py4e.com/code3/geojson.py. The program will
prompt for a location, contact a web service and retrieve JSON for the web
service and parse that data, and retrieve the first place_id from the JSON. A
place ID is a textual identifier that uniquely identifies a place as within
Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a
static subset of the Google Data:

http://py4e-data.dr-chuck.net/geojson?

This API uses the same parameter (address) as the Google API. This API also
has no rate limit so you can test as often as you like. If you visit the URL
with no parameters, you get a list of all of the address values which can be
used with this API.

To call the API, you need to provide address that you are requesting as the
address= parameter that is properly URL encoded using the urllib.urlencode()
fuction as shown in http://www.py4e.com/code3/geojson.py

Turn In

Please run your program to find the place_id for this location:

Washington State University

"""

import urllib.request, urllib.parse, json, ssl

# Set up api key
api_key = False
if api_key == False:
    api_key = 42
    service_url = "https://py4e-data.dr-chuck.net/geojson?"

# Ignore SSL cert
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Ask user for location
    location = input("Enter Location: ")
    if len(location) < 1: break
    
    parms = dict()
    parms['address'] = location
    if api_key != False: parms['key'] = api_key
    
    # Compute true url using location and open url to request JSON data
    url = service_url + urllib.parse.urlencode(parms)
    rawData = urllib.request.urlopen(url, context=ctx)
    data = rawData.read().decode()
    jsonData = json.loads(data)

    print(jsonData)
    
    # Extract place_id
    place_id = jsonData['results'][0]['place_id']
    print("\nPlace ID: ", place_id)


