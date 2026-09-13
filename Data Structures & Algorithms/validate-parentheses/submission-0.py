class Solution:
    def isValid(self, s: str) -> bool:
        # Time is O(n) since we're only going through every input character once
        # Memory is O(n) since we are using a stack, the stack could be up to the size of the input
        
        if len(s) % 2 == 1:
            return False

        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # Maps the close parantheses to the open parantheses
        for c in s:
            # check if c is in closeToOpen (aka if c is a closing parantheses)
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]: # if stack exists (not empty) 
                # and the last value we added to the stack is the same type of parantheses 
                # but an opening parantheses then we pop the parantheses off the stack
                # since it is valid 
                    stack.pop()
                
                # If the parantheses don't match each other or the stack is empty (starting with a closing parantheses) return false
                else:
                    return False

            # if c is not a closing parntheses then pop it onto the stack
            else:
                stack.append(c)

        # Can only return true if stack is empty, when stack is empty that means all parantheses are valid
        return True if not stack else False

            