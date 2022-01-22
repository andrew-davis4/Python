import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://api.opencovid.ca/other?stat=prov'
data = requests.get(url).text

json_data = json.loads(data)

print(json_data)