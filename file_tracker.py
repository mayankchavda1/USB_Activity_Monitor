from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from logger import log_event

class USBFileHandler(FileSystemEventHandler):

    def on_created(self,event):

        if not event.is_directory:

            log_event(
                "FILE_CREATED",
                event.src_path
            )

            if event.src_pah.endswth(".exe"):

                log_event(
                    "EXECUTABLE_DETECTED",
                    event.src_path
                )

def start_file_monitor(path):

    event_handler  = USBFileHandler()

    observer =  Observer(
        event_handler,
        path,
        recursive=True

    )

    observer.start()

    return  observer


