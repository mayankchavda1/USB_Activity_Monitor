from monitor import monitor_usb
from colorama import init, Fore

init()

print(Fore.GREEN + "=" * 50)
print(Fore.GREEN + "USB ACTIVITY MONITOR STARTED")
print(Fore.GREEN + "=" * 50)

monitor_usb()

