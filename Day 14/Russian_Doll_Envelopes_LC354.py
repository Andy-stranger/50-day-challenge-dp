from bisect import bisect_left

def maxEnvelopes(self, envelopes) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x : (x[0],-x[1]))
        hts = [e[1] for e in envelopes]
        res = []
        for ht in hts:
            pos = bisect_left(res, ht)
            if pos == len(res):
                res.append(ht)
            else:
                res[pos] = ht
        return len(res)