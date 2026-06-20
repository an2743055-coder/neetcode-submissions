class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":    # ✅ s not str
                j += 1
            length = int(s[i:j])  # ✅ slice i to j, not str(i+j)
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res