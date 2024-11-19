#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the process of merging the lists
        dummy = ListNode()
        # 'cur' will be used to build the merged list
        cur = dummy

        # Iterate through both lists until one of them is fully processed
        while list1 and list2:
            # Compare the current values of both lists
            if list1.val > list2.val:
                # If list2's value is smaller, append it to the merged list
                cur.next = list2
                # Move list2 to the next node
                list2 = list2.next
            else:
                # If list1's value is smaller or equal, append it to the merged list
                cur.next = list1
                # Move list1 to the next node
                list1 = list1.next
            
            # Move 'cur' to the next node in the merged list
            cur = cur.next
        
        # Once one of the lists is exhausted, append the remaining nodes of the other list
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        # Return the merged list, starting from the first node (dummy.next)
        return dummy.next
