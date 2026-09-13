class Solution:
    def isPalindrome(self, s: str) -> bool:
# Solution uses extra memory by creating newStr and reversing the string O(n) memory
# Solution is O(n) time complexity where n is length of the str
        newStr = "" # Create a new string

        for c in s: # Loop over each character in the original string
            if c.isalnum(): # Check if the character is alpha-numeric
                newStr += c.lower() # If it is alpha-numeric then only insert it into the new string 
        return newStr == newStr[::-1] # check if the newStr is equal to the newStr reversed