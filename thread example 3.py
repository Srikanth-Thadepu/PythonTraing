import threading
import time

print("Printing numbers")
def even():
    for i in range(6):
        if i%2==0:
            print(i)

def odd():
    for i in range(6):
        if i%2!=0:
            print(i)

thread1=threading.Thread(target=even)
thread2=threading.Thread(target=odd)
time.sleep(2)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
print("the numbers are printed")