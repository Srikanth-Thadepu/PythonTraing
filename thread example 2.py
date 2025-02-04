import threading
import time

print("Preparing the ppt")
def add_image():
    print("Adding images to the ppt")
    time.sleep(2)
    print("Added relevent images to the ppt")

thread=threading.Thread(target=add_image)
thread.start()
thread.join()
print("Presented the ppt")