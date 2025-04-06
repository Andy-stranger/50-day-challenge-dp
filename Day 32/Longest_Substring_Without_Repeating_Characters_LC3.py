def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)
    chars = set()
    l = 0
    res = 1
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        res = max(res,r-l+1)
    return res