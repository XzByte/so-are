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
from ScriptScan.cvaudit2 import fetch_cve_data
from ScriptScan.ScanOldSw import scan_old_software

def main():
    print("""
          Menu:
             automate? y/N?
                       
             Your answer: """)
    opt = input(str(">>> ")).lower()

    if opt == "y":
        print("""It's the automated interface of SO-ARE?\n
              included auto Remediation and reporting""")
        
        scanner = scan_old_software()
        outdated_packages = scanner.check_for_updates()
        for package_name, package_version in outdated_packages:
            fetch_cve_data(package_name, package_version)

    elif opt == 'n':
        print("""it's the manual interface of SO-ARE?\n
              Here's the menu :
              1. Scan for old software
              2. Scan for IDOR (Insecure Direct Object Reference) vulnerabilities""")
    else:
        print("Invalid option. Please enter 'y' for automated or 'n' for manual.")

if __name__ == "__main__":
    main()
