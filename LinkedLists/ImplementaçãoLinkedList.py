class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Funções da Linked List

    def add_to_front(self, value):
        new_node = Node(value)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node

    def add_to_back(self, value):
        new_node = Node(value)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def remove_front(self):

        if not self.head: # Está nulo
            return None

        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value
    
    def remove_back(self):

        if not self.tail:
            return None
    
        removed_value = self.head.value
        if self.tail == self.head:
            self.head = self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return removed_value
    


dll = DoublyLinkedList()

print("pop front (vazia):", dll.remove_front())  # None
print("pop back (vazia):", dll.remove_back())    # None

dll.add_to_front(10)     # [10]
dll.add_to_front(20)     # [20] <-> [10]
dll.add_to_back(5)       # [20] <-> [10] <-> [5]

print(dll.remove_front())  # 20 -> [10] <-> [5]
print(dll.remove_back())   # 5  -> [10]
print(dll.remove_front())  # 10 -> []
print(dll.remove_back())   # None (vazia)