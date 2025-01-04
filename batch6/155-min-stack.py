class MinStack:

    def __init__(self):
        self.main_stack, self.min_stack = [], [float('inf')]

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        top_element = self.top()
        self.main_stack.pop()
        if top_element == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
