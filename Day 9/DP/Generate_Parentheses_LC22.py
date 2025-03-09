from typing import List

def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def recur(openn,closee,cur):
        if openn == closee and len(cur) == 2*n:
            res.append(cur)
            return
        if openn < n:
            recur(openn+1,closee,cur+'(')
        if closee < openn:
            recur(openn,closee+1,cur+')')
        return
    recur(0,0,'')
    return res