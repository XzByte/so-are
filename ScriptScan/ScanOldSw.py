import subprocess
class scan_old_software:
    def __init__(self):
        print("""
              This is just the prototype of scanner, only scanner""")
    def check_for_updates():
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        result = subprocess.run(["sudo", "apt-get", "upgrade", "--simulate"], capture_output=True, text=True, check=True)

        if result.stdout:
            print("Outdated packages:")
            print(result.stdout)
        else:
            print("No outdated packages found.")

if __name__ == "__main__":
    scan_old_software.check_for_updates()
        