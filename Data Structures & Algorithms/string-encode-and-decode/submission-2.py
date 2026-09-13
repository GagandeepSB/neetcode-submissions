class Solution:
    def encode(self, strs: List[str]) -> str:
        res = "".join(f"{len(st)}#{st}" for st in strs)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count = 0
        prev = 0
        i = 0

        while i < len(s):
            while s[i] != "#":
                i += 1
                continue

            count = int(s[prev:i])
            #print('count', count)
            #print('s[prev:i]', s[prev:i])
            res.append(s[i+1:(count+i+1)])
            #print('res', res)
            i += count+1
            #print('i after inc', i)
            prev = i
            #print('prev after setting to i', prev)
        
        return res