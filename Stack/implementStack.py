from collections import deque

# Class to implement a stack using deque
class stack: 
    def __init__(self):
        # Initialize an empty deque to store stack elements
        self.container = deque()
    
    def push(self, value): 
        """
        Add an element to the top of the stack.
        Append the value to the right end of the deque (push).
        """
        self.container.append(value)
    
    def pop(self): 
        """
        Remove the top element from the stack.
        Pop from the right end of the deque (pop).
        """
        self.container.pop()
    
    def peek(self):
        """
        Return the top element of the stack without removing it.
        Get the last element of the deque.
        """
        return self.container[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        Return True if the deque is empty, False otherwise.
        """
        if len(self.container) == 0:
            return True 
        else:
            return False
    
    def size(self):
        """
        Return the current size of the stack.
        """
        return len(self.container)

# Create an instance of the stack
st = stack()

# Input string to reverse
string = "We will conquere COVID-19"

# Push each character of the string onto the stack
for char in string: 
    st.push(char)

# Initialize an empty list to hold the reversed string
reverse_string = []

# Pop each character from the stack and append it to reverse_string
# The stack follows Last In, First Out (LIFO) order, which helps reverse the string
while st.is_empty() == False: 
    reverse_string.append(st.peek())  # Get the top element (peek) and add to the list
    st.pop()  # Remove the top element (pop)

# Join the reversed characters to form the reversed string
reverse_string = ''.join(reverse_string)

# Print the reversed string
print(reverse_string)
