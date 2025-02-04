import time
import threading
import queue

def producer(q):
    for i in range(5):
        time.sleep(1)  # Simulate some work with a sleep
        item = f"Item {i}"
        q.put(item)
        print(f"Produced {item}")
    q.put(None)  # Signal the consumer to stop

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Processing complete.")