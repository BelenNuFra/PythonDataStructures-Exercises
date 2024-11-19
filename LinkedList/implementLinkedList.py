class Node:
    def __init__(self, data=None, next=None):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

    def print(self):
        # Print all elements in the linked list
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head  # Start from the head node
        llstr = ''  # Initialize an empty string to store the result
        while itr:
            # Append the current node's data to the string
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next  # Move to the next node
        print(llstr)

    def get_length(self):
        # Calculate the length of the linked list
        count = 0
        itr = self.head  # Start from the head node
        while itr:
            count += 1  # Increment the counter for each node
            itr = itr.next  # Move to the next node
        return count

    def insert_at_begining(self, data):
        # Insert a node at the beginning of the linked list
        node = Node(data, self.head)  # Create a new node pointing to the current head
        self.head = node  # Update the head to the new node

    def insert_at_end(self, data):
        # Insert a node at the end of the linked list
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = Node(data, None)
            return

        itr = self.head  # Start from the head node
        while itr.next:
            itr = itr.next  # Traverse to the last node

        itr.next = Node(data, None)  # Create a new node at the end

    def insert_at(self, index, data):
        # Insert a node at a specific index
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            # If inserting at the beginning, use the existing method
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head  # Start from the head node
        while itr:
            if count == index - 1:
                # Insert the new node at the desired position
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next  # Move to the next node
            count += 1

    def remove_at(self, index):
        # Remove a node at a specific index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            # If removing the first node, update the head
            self.head = self.head.next
            return

        count = 0
        itr = self.head  # Start from the head node
        while itr:
            if count == index - 1:
                # Update the pointer to skip the node at the index
                itr.next = itr.next.next
                break
            itr = itr.next  # Move to the next node
            count += 1

    def insert_values(self, data_list):
        # Insert multiple values into the linked list
        self.head = None  # Reset the list
        for data in data_list:
            self.insert_at_end(data)  # Add each value to the end

    def insert_after_value(self, data_after, data_to_insert):
        # Insert a new node after a specific value
        itr = self.head  # Start from the head node

        if itr is None:
            # If the list is empty, print a message
            print("The linked list is empty")
            return

        while itr:
            if itr.data == data_after:
                # If the value is found, insert the new node
                new_node = Node(data_to_insert, itr.next)
                itr.next = new_node
                return
            itr = itr.next  # Move to the next node

    def remove_by_value(self, data):
        # Remove a node by its value
        itr = self.head  # Start from the head node

        if itr is None:
            # If the list is empty, print a message
            print("The linked list is empty")
            return

        if itr.data == data:
            # If the value is at the head, update the head
            self.head = self.head.next
            return

        while itr.next:
            if itr.next.data == data:
                # Update the pointer to skip the node with the value
                itr.next = itr.next.next
                return
            itr = itr.next

        # If the value is not found, print a message
        print("The value is not in the linked list")


if __name__ == '__main__':
    ll = LinkedList()
    # Insert values into the linked list
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    
    # Try removing a value not in the list
    ll.remove_by_value("figs")
    ll.print()
    
    # Remove the head node
    ll.remove_by_value("banana")
    ll.print()
    
    # Remove another node
    ll.remove_by_value("mango")
    ll.print()
    
    # Try removing a value not in the list
    ll.remove_by_value("apple")
    ll.print()
    
    # Remove the last two nodes
    ll.remove_by_value("grapes")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
