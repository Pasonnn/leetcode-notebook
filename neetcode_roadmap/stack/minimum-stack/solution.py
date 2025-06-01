class MinStack:

    def __init__(self):
        self.stack = [] # Initialize the stack
        
    def push(self, val: int) -> None:
        self.stack.append(val) # Append the value to the top (end) of the stack
        return None
        
    def pop(self) -> None:
        self.stack.pop() # Pop the last element from the stack
        return None

    def top(self) -> int:
        return self.stack[-1] # Return the last element from the stack

    def getMin(self) -> int:
        return min(self.stack) # Return the minimum value from the stack