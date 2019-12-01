class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            # save current appending value as min value at the same time if stack is empty
            self.stack.append((x, x))
        else:
            # if stack is not empty, identify current min with appending value and save
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()  # remove the last tuple from stack

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]  # get (x,min) 's  -> x
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]  # get (x, min) 's -> min
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
