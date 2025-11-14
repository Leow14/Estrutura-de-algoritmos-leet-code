# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        new_list = ListNode(0)
        new_list_pointer = new_list

        # Verifica se uma das listas é vazia, se for, retorna a outra, se ambas forem, retorna None

        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list1 and not list2:
            return None

        # Concaneta as listas uma na outra, com base no menor "head"

        while list1 and list2:
            if list2.val > list1.val:
                new_list.next = list1
                list1 = list1.next  
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
            
        # Como estou utilizando a comparação "and", talvez sobre algum residual de outra lista, nessa parte concatenamos esse residual ao novo head

        if list1:
            new_list.next = list1
        else:
            new_list.next = list2
        
        return new_list_pointer.next
