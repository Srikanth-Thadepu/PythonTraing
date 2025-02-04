import threading
import time

class TicketBooking:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
        self.available_tickets = 10

    def book_ticket(self, tickets_requested):
        with self.lock:
            print(f"{self.name} is attempting to book {tickets_requested} tickets.")
            if self.available_tickets >= tickets_requested:
                time.sleep(1)  # Simulate the time taken to book tickets
                self.available_tickets -= tickets_requested
                print(f"{self.name} successfully booked {tickets_requested} tickets.")
            else:
                print(f"Not enough tickets available for {self.name} to book {tickets_requested} tickets.")
            print(f"Tickets remaining: {self.available_tickets}")

def book_tickets(name, tickets_requested, booking_system):
    booking_system.book_ticket(tickets_requested)

booking_system = TicketBooking("BookingSystem")

threads = []
customers = [("Alice", 3), ("Bob", 4), ("Charlie", 2), ("Dave", 5)]

for customer in customers:
    thread = threading.Thread(target=book_tickets, args=(customer[0], customer[1], booking_system))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All ticket booking attempts have been processed.")