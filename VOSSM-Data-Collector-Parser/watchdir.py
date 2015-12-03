# A watchdog file which checks filesystem for a new incoming file.
# Invokes parseFile when a new file is created.

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from parse import parseFile
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        parseFile(event.src_path);


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    project_root = os.environ.get('vossm_root')
    path = project_root + '/raw_data' 
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


 

