import requests
import json

url = "https://api.osv.dev/v1/query"
data = {
    "package": {"name": "mruby"},
    "version": "2.1.2rc"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)