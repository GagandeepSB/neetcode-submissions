class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if len not same, then not anagram
            return False # so return false
        countS, countT = {}, {}

        for i in range(len(s)): # since len is same for both strings, can use same index for both strings
            countS[s[i]] = 1 + countS.get(s[i], 0) # add 1 to the value of each key in the hashmap if it exists
            countT[t[i]] = 1 + countT.get(t[i], 0) # if character does not exist, then add it to the hashmap, get returns 0 and then add 1 to markt this as the first occurence
        for c in countS:
            if countS[c] != countT.get(c, 0): # If key in s does not exist in the t map, then return 0
                return False
        return True