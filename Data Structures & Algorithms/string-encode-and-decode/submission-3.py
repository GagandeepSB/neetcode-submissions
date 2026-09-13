class Solution:
    def encode(self, strs: List[str]) -> str:
        res = "".join(
            f"{len(st)}#{st}"
            for st in strs
        )

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j + 1: length + j + 1])
            i = j + 1 + length
        
        return res