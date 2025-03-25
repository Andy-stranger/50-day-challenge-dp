def isIsomorphic(s: str, t: str) -> bool:
    mapp = {}
    n = len(s)
    for i in range(n):
        key = s[i]
        val = t[i]
        if key in mapp and mapp[key] != val:
            return False
        if key not in mapp and val in mapp.values():
            return False
        mapp[key] = val
    return True