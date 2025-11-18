# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        tail = ListNode(None)
        dummy = tail

        if head1 and not head2:
            return head1
        elif not head1 and head2:
            return head2
        elif not head1 and not head2:
            return None

        while head1 and head2:
            if head1 > head2:
                tail.next = head2
                head2 = head2.next
            else:
                tail.next = head1
                head1 = head1.next
            tail = tail.next
        
        if head1:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next
