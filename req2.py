import requests
import json

url = "https://api.osv.dev/v1/query"
data = {
    "package": {"name": "mruby"},
    "version": "2.1.2rc"
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    try:
        response_data = response.json()
        for vuln in response_data.get('vulns', []):
            cve_id = vuln.get('id')
            summary = vuln.get('summary')
            details = vuln.get('details')
            print(f"CVE ID: {cve_id}")
            print(f"Summary: {summary}")
            print(f"Details: {details}")
            print("---")
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON.")
        print(response.text)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")