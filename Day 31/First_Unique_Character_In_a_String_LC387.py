from collections import defaultdict

def firstUniqChar(self, s: str) -> int:
    mapp = defaultdict(int)
    for ch in s:
        mapp[ch] += 1
    for i,ch in enumerate(s):
        if mapp[ch] == 1:
            return i
    return -1