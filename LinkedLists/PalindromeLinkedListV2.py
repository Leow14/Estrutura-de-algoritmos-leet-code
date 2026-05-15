# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            next_node = slow.next
            next_fast = fast.next.next
            slow.next = prev
            prev = slow
            slow = next_node
            fast = next_fast

        if fast: # This means the len of the linkedList is odd
            slow = slow.next

        while slow and prev:
            if slow.val == prev.val:
                slow = slow.next
                prev = prev.next
            else:
                return False
        return True