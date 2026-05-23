# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_string = ""
        l2_string = ""

        while l1.val and l1.next.val:
            l1_string = l1_string + str(l1.val)
            l1 = l1.next
        
        while l2.val and l2.next.val:
            l2_string = l2_string + str(l2.val)
            l2 = l2.next

        int_l1 = int(l1_string)
        int_l2 = int(l2_string)

        total = int_l1 + int_l2

        return total