import subprocess

class scan_old_software:
    def __init__(self):
        print("""
              This is just the prototype of scanner, only scanner""")

    def check_for_updates(self):
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        result = subprocess.run(["sudo", "apt-get", "upgrade", "--simulate"], capture_output=True, text=True, check=True)

        if result.stdout:
            print("Outdated packages:")
            outdated_packages = []
            for line in result.stdout.splitlines():
                if line.startswith("Inst"):
                    package_info = line.split()
                    package_name = package_info[1]
                    package_version = package_info[2]
                    outdated_packages.append((package_name, package_version))
            return outdated_packages
        else:
            print("No outdated packages found.")
            return []