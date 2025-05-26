class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0] # Initialize the stack with a 0
        paren_close_open = { # Create a dictionary to map the closing parentheses to the opening parentheses
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        close_paren = "}])" # Create a string of the closing parentheses
        open_paren = "{[(" # Create a string of the opening parentheses
        open_count = 0 # Initialize the open count
        close_count = 0 # Initialize the close count
        for paren in s:
            if paren in open_paren: # If the parenthesis is an opening parenthesis
                open_count += 1 # Increment the open count
                stack.append(paren) # Append the parenthesis to the stack
                
            if paren in close_paren: # If the parenthesis is a closing parenthesis
                close_count += 1 # Increment the close count
                if stack[-1] != paren_close_open[paren]: # If the last element in the stack is not the opening parenthesis for the closing parenthesis
                    return False # Return False
                stack.pop() # If the last element in the stack is the opening parenthesis for the closing parenthesis, Pop the last element from the stack
        if open_count != close_count: # If the open count is not equal to the close count
            return False # Return False
        return True # Return True