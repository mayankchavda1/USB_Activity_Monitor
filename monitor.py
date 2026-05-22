import psutil
import time
from logger import log_event

connected_devices = {}

def get_usb_drives():

    drives = []

    partitions = psutil.disk_partitions()

    for partition in partitions:

        if 'removable' in partition.opts.lower():

            drives.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype
            })

    return drives

def monitor_usb():
    global connected_devices

    while True:

        current_drives = get_usb_drives()

        current_set = set(
            drive["device"]
            for drive in current_drives
        )

        previous_set = set(
            connected_devices.keys()
        )

        inserted = current_set - previous_set

        removed = previous_set - current_set

        for drive in current_drives:

            if drive["device"] in inserted:

                connected_devices[drive["device"]] = time.time()

                log_event(
                    "USB_INSERTED",
                    f"{drive['device']} | "
                    f"{drive['mountpoint']} | "
                    f"{drive['fstype']}"
                )

        for device in removed:

            duration = int(
                time.time() - connected_devices[device]
            )

            log_event(
                "USB_REMOVED",
                f"{device} | "
                f"Session Duration: {duration}s"
            )

            del connected_devices[device]

        time.sleep(3)