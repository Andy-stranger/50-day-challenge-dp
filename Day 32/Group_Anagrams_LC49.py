from collections import defaultdict

def groupAnagrams(self, strs):
    res = defaultdict(list)
    for s in strs:
        chArr = list(s)
        chArr.sort()
        res[tuple(chArr)].append(s)
    return list(res.values())