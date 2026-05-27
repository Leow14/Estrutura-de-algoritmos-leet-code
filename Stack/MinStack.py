class MinStack:
    def __init__(self):
        self.stack       = []
        self.min_stack   = []

    def push(self, val: int) -> None:
        if self.min_stack:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


ms = MinStack()

ms.push(-2)
print(ms.stack, ms.min_stack)
ms.push(0)
print(ms.stack, ms.min_stack)
ms.push(-3)
print(ms.stack, ms.min_stack)
print(ms.getMin())
print(ms.stack, ms.min_stack)
print(ms.pop())
print(ms.stack, ms.min_stack)
print(ms.top())
print(ms.stack, ms.min_stack)
print(ms.getMin())
print(ms.stack, ms.min_stack)
