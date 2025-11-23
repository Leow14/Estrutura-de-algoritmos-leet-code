# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next 
        return head