import subprocess

class scan_old_software:
    def __init__(self):
        print("""
              This is just the prototype of scanner, only scanner""")

    def check_for_updates(self):
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        # Capture the output of the simulate upgrade command
        result = subprocess.run(["sudo", "apt-get", "upgrade", "--simulate"], capture_output=True, text=True, check=True)

        if result.stdout:
            print("Outdated packages:")
            # Parse the output to extract package names and versions
            outdated_packages = [line.split()[1] for line in result.stdout.splitlines() if line.startswith("Inst")]
            return outdated_packages
        else:
            print("No outdated packages found.")
            return []

if __name__ == "__main__":
    instance = scan_old_software()
    outdated_packages = instance.check_for_updates()
    print(outdated_packages)
import subprocess
