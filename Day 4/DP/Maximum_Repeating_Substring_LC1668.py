def maxRepeating(self, sequence: str, word: str) -> int:
    temp = word
    res = 0
    while temp in sequence:
        res += 1
        temp += word
    return res