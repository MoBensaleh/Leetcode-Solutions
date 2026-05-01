# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        p1 = l1
        p2 = l2

        while p1 or p2 or carry != 0:
            if p1:
                x = p1.val
            else:
                x=0
            

            if p2:
                y = p2.val
            else:
                y = 0
            
            sum_val = x + y + carry

            new_digit = sum_val % 10
            carry = sum_val // 10
            new_node = ListNode(new_digit)
            current.next = new_node
            current = current.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            
        return dummy.next

    
    # l1 = 2 -> 4 -> 3
    # l2 = 5 -> 6 -> 4

    