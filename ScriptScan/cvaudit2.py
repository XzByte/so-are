import sys
import requests
import json

# Add the ScriptScan directory to the Python path
sys.path.append('ScriptScan/')

from ScanOldSw import scan_old_software

# ... rest of your code ...

def fetch_cve_data(package_name, package_version):
    """
    Fetches data for a specific package name and version from the OSV API.
    """
    url = "https://api.osv.dev/v1/query"
    data = {
        "package": {
            "name": package_name},
            "version": package_version
        
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
        print(f"Failed to fetch data for package {package_name} version {package_version}. Status code: {response.status_code}")
        return None

def main():
    # Instantiate the scan_old_software class
    scanner = scan_old_software()
    # Get the list of outdated packages
    outdated_packages = scanner.check_for_updates()
    # Iterate over the outdated packages and fetch CVE data for each
    for package_name, package_version in outdated_packages:
        fetch_cve_data(package_name, package_version)

if __name__ == "__main__":
    main()
