import json
import urllib.request
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("People in space - " + str(result['number']))
people = result['people']
for p in people:
    print(p['name'] + " in the " + p['craft'])
url2 = http://api.open-notify.org/iss-now.json
response2 = urllib.request.urlopen(url)
result2 = json.loads(response.read())
location = result2['iss_position']
la = float(location['latitude'])
lo = float(location['longitude'])
print("Location - " + location)
print("Latitude - " + la)
print("Longitude - " + lo)