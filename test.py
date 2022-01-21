import requests
import json

print(json.loads(requests.get('https://api.opencovid.ca/').text))



