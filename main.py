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
      1. Scan for old software
      2. Check IDOR vulnerability
                
      Your answer: ''')
opt = input(str(">>> "))

if opt == 1:
      from ScriptScan import ScanOldSw
      print("Scanning for old software...")
      ScanOldSw.scan_old_software.check_for_updates()
elif opt == 2:
      from ScriptScan.IDORD.Wrapper import IDORD as idord
      print("Checking for IDOR...")
      instance = idord()
# ScanOldSw.scan_old_software.check_for_updates()
# instance = idord()
    