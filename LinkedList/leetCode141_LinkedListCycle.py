#Given head, the head of a linked list, determine if the linked list has a cycle in it.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Return true if there is a cycle in the linked list. Otherwise, return false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Step 1: Check if the list is too short to contain a cycle (empty or only one element)
        if not head or not head.next:  # If the list is empty or only has one element, no cycle is possible
            return False
        
        # Step 2: Initialize two pointers: slow and fast
        slow = head  # Slow pointer moves one step at a time
        fast = head.next  # Fast pointer moves two steps at a time (starts one step ahead of slow)
        
        # Step 3: Traverse the list with slow and fast pointers
        while slow != fast:  # While slow and fast pointers are not meeting (no cycle)
            if not fast or not fast.next:  # If fast reaches the end (None or next is None), no cycle exists
                return False
            slow = slow.next  # Move slow pointer one step forward
            fast = fast.next.next  # Move fast pointer two steps forward

        # Step 4: If slow and fast pointers meet, a cycle is detected
        return True  # Return True if a cycle is found
