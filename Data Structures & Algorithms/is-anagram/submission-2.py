class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {} # declaring two hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # for each character in s at index i (this is the key) is seen, add 1 to it 
            countT[t[i]] = 1 + countT.get(t[i], 0) # 0 is a default value that is returned if the key does not exist in the hashmap yet
        for c in countS:
            if countS[c] != countT.get(c, -1):
                return False
        return True # means it is an anagram
            
        