# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = None
        while head:
            next_node = head.next # Criamos o "próximo nodo", para armazenar o próximo nodo depois do head
            head.next = new_list # Agora setamos o próximo nodo do head como sendo o new_list, desvinculando da lista
            new_list = head # Agora new_list recebe o ponteiro head, indicando que é o começo da lista. 
            head = next_node # Agoa o head anda para o next node, para iniciarmos o loop novamente
            
        return new_list

