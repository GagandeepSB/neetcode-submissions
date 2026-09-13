class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Time complexity O(n) since we're iterating over every single input and
        # pop and append is O(1) operation and
        # Taking the sum of the stack is also a O(n) operation

        stack = []
        
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else: # Last case is if op is a number
                stack.append(int(op)) 
                # Convert op to an integer and append that to the stack
                # By doing this all values in the stack are integers and there is no need
                # To typecast to an integer every time we are psuhing onto the stack

        return sum(stack)       