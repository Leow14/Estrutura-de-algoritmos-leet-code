
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top    = None
        self._size = 0

    def push(self, val):
        new_node = Node(val=val)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self._size <= 0:
            raise IndexError("Stack is empty")

        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.val

    def peek(self):
        if self._size <= 0:
            raise IndexError("Stack is empty")
        return self.top.val

    def is_empty(self):
        if self._size <= 0:
            return True
        return False

    def size(self):
        return self._size
    

stack = Stack()

print(stack.is_empty())
stack.push(1)
stack.push(3)
stack.push(0)
stack.push(4)
stack.push(4)
print(stack.peek())
print(stack.size())
stack.push(8)
stack.push(7)
print(stack.peek())
stack.push(0)
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
print(stack.pop())
