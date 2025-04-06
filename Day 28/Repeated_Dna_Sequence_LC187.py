from collections import defaultdict

def findRepeatedDnaSequences(self, s: str):
    n = len(s)
    if n <= 10:
        return []
    mapp = defaultdict(int)
    left = 0
    right = 9
    while right < n:
        mapp[s[left:right+1]] += 1
        left += 1
        right += 1
    res = []
    for key , val in mapp.items():
        if val > 1:
            res.append(key)
    return res