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
        new_list = ListNode(None)
        new_list_indicator = None
        next_node1 = head1.next
        next_node2 = head2.next
    
        ## List1 = head1 || List2 = head2
        while head1 and head2:
            if head1.value < head2.value:
                new_list.next = head1
                new_list_indicator = head1
                head1.next = head1
                next_node1 = head1.next
            else:
                new_list.next = head2
                new_list_indicator = head2
                head2.next = head2
                next_node2 = head2.next

        return new_list


