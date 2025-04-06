from collections import defaultdict

def minWindow(self, s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    tMap = defaultdict(int)
    for ch in t:
        tMap[ch] += 1
    left = 0
    right = 0
    start = -1
    min_len = float("inf")
    count = 0
    while right < n:
        if tMap[s[right]] > 0:
            count += 1
        tMap[s[right]] -= 1
        while left <= right and count == m:
            if min_len > right-left+1:
                min_len = right - left + 1
                start = left
            tMap[s[left]] += 1
            if tMap[s[left]] > 0:
                count -= 1
            left += 1
        right += 1
    if start == -1:
        return ""
    return s[start:start+min_len]