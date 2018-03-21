import betterthreads
import socket
import time


class StoppableThread(betterthreads.Thread):
    def run(self):
        print("Listening on ")

    def shutdown():
        print("Shutting down cleanly...")

if __name__ == '__main__':
    t = StoppableThread()
    t.start()
    print("Press <Ctrl-C> to stop thread")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit("Keyboard interrupt - waiting for thread to finish...")
