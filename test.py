import requests
import json

print(json.loads(requests.get('https://api.opencovid.ca/').text))



# //andrew-davis4
# //8c93hfakweu