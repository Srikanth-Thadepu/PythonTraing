import threading
import time

def single_task():
    print("Task Started")
    time.sleep(2)
    print("Task Completed")

thread=threading.Thread(target=single_task)
thread.start()
thread.join()
print("Main thread executed")