class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addToFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
        self.head = newNode

    def addToBack(self, value):
        newNode = Node(value)
        if self.tail is None:
            self.head = newNode
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def removeFromFront(self): # função como o pop, retorna o valor removido
        if self.head is None: # lista vazia
            return None
        removedValue = self.head.value
        if self.head == self.tail: # lista com um só índice
            self.head = self.tail = None
            return removedValue
        else:
            self.head = self.head.next
            self.head.previous = None
        return removedValue
    
    def removeFromBack(self):
        if self.tail is None: # lista vazia
            return None
        removedValue = self.tail.value
        if self.tail == self.head: # lista com um só índice
            self.tail = self.head = None
            return removedValue
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return removedValue


dll = DoubleLinkedList()

print("pop front (vazia):", dll.removeFromFront())  # None
print("pop back (vazia):", dll.removeFromBack())    # None

dll.addToFront(10)     # [10]
dll.addToFront(20)     # [20] <-> [10]
dll.addToBack(5)       # [20] <-> [10] <-> [5]

print(dll.removeFromFront())  # 20 -> [10] <-> [5]
print(dll.removeFromBack())   # 5  -> [10]
print(dll.removeFromFront())  # 10 -> []
print(dll.removeFromBack())   # None (vazia)