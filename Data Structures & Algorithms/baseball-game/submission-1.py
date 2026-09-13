class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for c in operations:
            if c == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
                #print(stack[-1])
            elif c == "C":
                stack.pop()
                #print(stack[-1])
            elif c == "D":
                stack.append(int(stack[-1]) * 2)
                #print(stack[-1])
            else:
                stack.append(c)
                #print(stack[-1])

        total = 0

        for i in stack:
            total += int(i)
        
        return total

        