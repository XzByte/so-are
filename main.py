print("""
      This is just the prototype of scanner, only scanner""")
import sys
sys.path.append('ScriptScan/')
sys.path.append('Remed/')

print("""
         
   ░██████╗░█████╗░░░░░░░░█████╗░██████╗░███████╗░█████╗░
   ██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ╚█████╗░██║░░██║█████╗███████║██████╔╝█████╗░░╚═╝███╔╝
   ░╚═══██╗██║░░██║╚════╝██╔══██║██╔══██╗██╔══╝░░░░░╚══╝░
   ██████╔╝╚█████╔╝░░░░░░██║░░██║██║░░██║███████╗░░░██╗░░
   ╚═════╝░░╚════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░""")
print('''Menu:
       automate? y/N?
                   
       Your answer: ''')
opt = input(str(">>> ")).lower()

if opt == "y":
      print("""It's the automated interface of SO-ARE?\n
            included auto Remediation and reporting""")
      
      from ScriptScan.ScanOldSw import scan_old_software
      from ScriptScan.cvaudit import fetch_cve_ids_for_package, fetch_cve_data, identify_vulnerabilities
      
      outdated_packages = scan_old_software().check_for_updates()
      print(f"Outdated packages found: {outdated_packages}")
      
      for package in outdated_packages:
          cve_ids = fetch_cve_ids_for_package(package)
          print(f"CVE IDs for {package}: {cve_ids}")
          
          for cve_id in cve_ids:
              cve_data = fetch_cve_data(cve_id)
              if cve_data:
                  print(f"CVE ID: {cve_data['cve']['CVE_data_meta']['ID']}")
                  print(f"Description: {cve_data['cve']['description']['description_data'][0]['value']}")
                  print(f"Severity: {cve_data['impact']['baseMetricV3']['cvssV3']['baseSeverity']}")
                  print(f"Affected Products: {cve_data['affects']['vendor']['vendor_data'][0]['product']['product_data'][0]['product_name']}")
                  print("Remediation Steps:")
              else:
                  print(f"No data found for CVE ID {cve_id}")
      
      print("Automatic vulnerability audit completed.")
elif opt == 'n':
      print("""it's the manual interface of SO-ARE?\n
            Here's the menu :
            1. Scan for old software
            2. Scan for IDOR (Insecure Direct Object Reference) vulnerabilities""")
# ScanOldSw.scan_old_software.check_for_updates()
# instance = idord()