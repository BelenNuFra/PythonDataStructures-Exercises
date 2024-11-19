from collections import deque
import time
import threading

# Class to implement a Queue using deque
class Queue:
    def __init__(self):
        # Initialize an empty deque to store queue elements
        self.buffer = deque()

    def enqueue(self, val):
        """
        Add an element to the queue.
        Append the value to the left side of the deque (enqueue).
        """
        self.buffer.appendleft(val)

    def dequeue(self):
        """
        Remove and return the oldest element in the queue.
        Pop from the right side of the deque (dequeue).
        """
        return self.buffer.pop()

    def is_empty(self):
        """
        Check if the queue is empty.
        Return True if the deque is empty, False otherwise.
        """
        return len(self.buffer) == 0

    def size(self):
        """
        Return the current size of the queue.
        """
        return len(self.buffer)

# Function to simulate placing orders into the queue
def place_order(orders, q):
    """
    Add each order from the list to the queue with a small delay.
    """
    for order in orders:
        q.enqueue(order)  # Add the order to the queue
        print(f"Order placed: {order}")  # Print confirmation
        time.sleep(0.5)  # Simulate a delay in placing orders
    return q

# Function to simulate serving orders from the queue
def serve_order(q):
    """
    Remove and process each order from the queue with a small delay.
    """
    while not q.is_empty():  # Continue until the queue is empty
        order = q.dequeue()  # Get the next order
        print(f"Order served: {order}")  # Print confirmation
        time.sleep(2)  # Simulate time taken to serve an order

# List of orders to be processed
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
q = Queue()  # Create an instance of the Queue class

# Create threads for placing and serving orders
t1 = threading.Thread(target=place_order, args=(orders, q))
t2 = threading.Thread(target=serve_order, args=(q,))

# Start placing orders
t1.start()
time.sleep(1)  # Short delay to allow some orders to be placed before serving starts

# Start serving orders
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
