import requests
from ScriptScan.ScanOldSw import scan_old_software

import requests
import json

def fetch_cve_ids_for_package(package_name, package_version):
    """
    Fetches CVE IDs for a specific package name and version from the OSV API.
    """
    url = "https://api.osv.dev/v1/query"
    headers = {'Content-Type': 'application/json'}
    data = {
        "package": {
            "name": package_name,
            "version": package_version
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch CVE IDs for package {package_name} version {package_version}. Status code: {response.status_code}")
        return []

def fetch_cve_data(cve_id):
    """
    Fetches data for a specific CVE ID from the NVD API.
    """
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    response = requests.get(url)
    
    if response.status_code ==  200:
        return response.json()
    else:
        print(f"Failed to fetch data for CVE ID {cve_id}. Status code: {response.status_code}")
        return None

def identify_vulnerabilities(outdated_packages):
    """
    Identifies vulnerabilities for the given outdated packages and provides remediation steps.
    """
    for package_name, package_version in outdated_packages:
        cve_ids = fetch_cve_ids_for_package(package_name, package_version)
        for cve_id in cve_ids:
            cve_data = fetch_cve_data(cve_id)
            if cve_data:
                print(f"CVE ID: {cve_data['cve']['CVE_data_meta']['ID']}")
                print(f"Description: {cve_data['cve']['description']['description_data'][0]['value']}")
                print(f"Severity: {cve_data['impact']['baseMetricV3']['cvssV3']['baseSeverity']}")
                print(f"Affected Products: {cve_data['affects']['vendor']['vendor_data'][0]['product']['product_data'][0]['product_name']}")
                print("Remediation Steps:")

def main():
    outdated_packages = scan_old_software().check_for_updates()
    identify_vulnerabilities(outdated_packages)

if __name__ == "__main__":
    main()
