
class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        self.curMin = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curMin = min(self.curMin , val)
        self.minStack.append(self.curMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]










