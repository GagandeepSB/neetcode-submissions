class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time O(n)
        # Memory O(n)
        stack = []

        for c in s:
            stack.append(c)
        
        index = 0
        while stack:
            s[index] = stack.pop()
            index += 1

