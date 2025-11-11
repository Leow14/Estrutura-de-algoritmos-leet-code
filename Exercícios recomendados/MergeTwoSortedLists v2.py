# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
       new_list = ListNode(0, None)
       while list1 and list2:
            if list2 > list1:
                new_list.next = list1
                list1.next = list1
                
                
            else:
                pass

