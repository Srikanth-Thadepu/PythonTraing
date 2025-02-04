import threading
import time

class Clock:
    def __init__(self):
        self.lock = threading.Lock()
        self.running = True

    def display_time(self):
        while self.running:
            with self.lock:
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"Current Time: {current_time}")
            time.sleep(1)

    def stop_clock(self):
        with self.lock:
            self.running = False

clock = Clock()

clock_thread = threading.Thread(target=clock.display_time)
clock_thread.daemon = True 
clock_thread.start()

time.sleep(10)
clock.stop_clock()

print("Clock has been stopped.")