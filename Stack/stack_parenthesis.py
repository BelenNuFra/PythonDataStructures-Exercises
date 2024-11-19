from collections import deque

# Defines the 'stack' class to implement a stack using deque
class stack: 
    def __init__(self):
        # Initializes the stack using deque (more efficient than a list for pop and append operations)
        self.container = deque()
    
    def push(self, value): 
        # Adds a value to the end of the stack (simulates 'push')
        self.container.append(value)
    
    def pop(self): 
        # Removes and returns the last value from the stack (simulates 'pop')
        self.container.pop()
    
    def peek(self):
        # Returns the last value of the stack without removing it (simulates 'peek')
        return self.container[-1]
    
    def is_empty(self):
        # Checks if the stack is empty, returns True if it is, False otherwise
        return len(self.container) == 0
    
    def size(self):
        # Returns the current size of the stack (number of elements)
        return len(self.container)

# Function that checks if the parentheses in a string are balanced
def is_balanced(value):
    # Create a new stack to handle the parentheses
    st = stack()
    # Map of opening and closing parentheses
    aMap = {"(": ")", "{": "}", "[": "]"}

    # Loop through each character in the string
    for i in value:
        # If the character is an opening parenthesis, push it to the stack
        if i == '(' or i == '{' or i == '[':
            st.push(i)
        # If the character is a closing parenthesis, check for balance
        if i == ')' or i == '}' or i == ']':
            # If the stack is empty, the parentheses are unbalanced
            if st.is_empty() == True:
                print("Not balanced")
                return False 
            # Check if the top of the stack matches the current closing parenthesis
            if i == ')' and st.pop() == '(' or i == ']' and st.pop() == '[' or i == '}' and st.pop() == '{':
                # If matched, pop the top element from the stack
                st.pop()
          
    # If the stack is empty at the end, the parentheses are balanced
    if st.is_empty() == True:
        print("Balanced")
        return 

# Test the function with various strings
is_balanced("({a+b})")  # Balanced
is_balanced("))((a+b}{")  # Not balanced
is_balanced("((a+b))")  # Balanced
is_balanced("((a+g))")  # Balanced
is_balanced("))")  # Not balanced
is_balanced("[a+b]*(x+2y)*{gg+kk}")  # Balanced
