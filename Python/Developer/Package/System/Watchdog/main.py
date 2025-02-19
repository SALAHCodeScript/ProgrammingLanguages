from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Define the event handler class
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'{event.src_path} has been created')
    def on_modified(self, event):
        print(f'{event.src_path} has been modified')
    def on_moved(self, event):
        print(f'{event.src_path} has been moved')
    def on_deleted(self, event):
        print(f'{event.src_path} has been deleted')

# Set up the observer and handler
observer = Observer()
event_handler = MyHandler()

# Specify the directory to watch
directory_to_watch = "D:\\Data\\SALAH\\Linux\\home\\salah\\Documents\\.programming\\Python\\Developer\\Package\\System\\Watchdog"

observer.schedule(event_handler, directory_to_watch, recursive=False)

# Start monitoring the directory
observer.start()

try:
    while True:
        time.sleep(1)  # Keep the program running
except KeyboardInterrupt:
    observer.stop()

observer.join()
