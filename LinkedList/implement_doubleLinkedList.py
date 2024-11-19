# Node class represents an individual node in the doubly linked list.
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data  # Data stored in the node
        self.next = next  # Pointer to the next node in the list
        self.prev = prev  # Pointer to the previous node in the list

# LinkedList class represents the doubly linked list structure.
class LinkedList: 
    def __init__(self):
        self.head = None  # Pointer to the first node (head) of the list

    def print_forward(self):
        """
        Print the list in forward direction using the 'next' pointer.
        """
        itr = self.head  # Start from the head of the list
        if itr == None:  # If the list is empty
            print("Lista vacía")  # Print a message indicating the list is empty
            return
        else:
            while itr:  # Traverse through the list until the end
                print(itr.data)  # Print the data of the current node
                itr = itr.next  # Move to the next node

    def insert(self, data):
        """
        Insert a new node at the end of the list.
        """
        if self.head == None:  # If the list is empty
            # Create a new node and set it as the head
            nuevo_nodo = Node(data)
            self.head = nuevo_nodo
        else:
            itr = self.head  # Start from the head of the list
            # Traverse the list to find the last node
            while itr.next:
                itr = itr.next
            # Create a new node and attach it at the end
            nuevo_nodo = Node(data)
            itr.next = nuevo_nodo  # Set the next of the last node to the new node
            nuevo_nodo.prev = itr  # Set the previous of the new node to the last node

    def print_backward(self):
        """
        Print the list in reverse order using the 'prev' pointer.
        """
        itr = self.head  # Start from the head of the list
        if itr == None:  # If the list is empty
            print("La lista está vacía")  # Print a message indicating the list is empty
        else:
            # Traverse to the last node
            while itr.next:
                itr = itr.next
            # Traverse backwards from the last node to the head
            while itr:
                print(itr.data)  # Print the data of the current node
                itr = itr.prev  # Move to the previous node


# Example usage of the LinkedList class
ll = LinkedList()
# Insert nodes with values "1", "2", "3", "4" into the list
ll.insert("1")
ll.insert("2")
ll.insert("3")
ll.insert("4")

# Print the list in forward direction
ll.print_forward()
# Print the list in backward direction
ll.print_backward()
