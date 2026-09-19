class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        Len = 0

        for st in strs:
            Len = str(len(st)) + "#"
            res += "".join(Len + st)
        
        return res
        
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            strs.append(s[j+1:j+length+1])
            i = length + j + 1

        return strs 