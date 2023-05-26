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


