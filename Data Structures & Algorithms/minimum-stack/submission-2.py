class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.sorted_stack:
            to_add = min(self.sorted_stack[-1], val)
            self.sorted_stack.append(to_add)
        else:
            self.sorted_stack.append(val)


    def pop(self) -> None:
        self.sorted_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_stack[-1]
