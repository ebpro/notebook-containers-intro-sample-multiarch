import platform
import os

def get_system_info():
    return {
        "arch": platform.machine(),
        "system": platform.system(),
        "hostname": os.uname().nodename
    }

if __name__ == "__main__":
    info = get_system_info()
    print(f"Hello from {info['arch']} running on {info['system']}")