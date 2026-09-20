class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            Len = str(len(st)) + "#"
            res += "".join(Len + st)

        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        
        return res
