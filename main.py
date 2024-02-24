print("""
      This is just the prototype of scanner, only scanner""")
import sys
sys.path.append('ScriptScan/')
sys.path.append('ScriptScan/idord/Wrapper/')
sys.path.append('Remed/')
from ScriptScan import ScanOldSw
from ScriptScan import idord 
if __name__ == "__main__":
    ScanOldSw.scan_old_software.check_for_updates()
    
    