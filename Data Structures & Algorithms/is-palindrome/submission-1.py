class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Two while loops below check if char is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # If char is alphanumeric then compare the two characters
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        # If the whole loop finishes, then the string is a palindrome
        return True

    def alphaNum(self, c):
        # can get ASCII value of a character using the ord function
        # ASCII values are contiguous (uppercase, lowercase, 0-9)
        return  (ord('A') <= ord(c) <= ord('Z') or
                 ord('a') <= ord(c) <= ord('z') or
                 ord('0') <= ord(c) <= ord('9'))