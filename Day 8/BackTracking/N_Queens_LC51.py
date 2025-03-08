from typing import List

def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = [['.' for _ in range(n)] for _ in range(n)]
        def boardToList(board):
            return [''.join(row) for row in board]
        def canFit(r,c,cur):
            for i in range(r):
                if cur[i][c] == 'Q':
                    return False
            for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
                if cur[i][j] == 'Q':
                    return False
            for i,j in zip(range(r,-1,-1),range(c,n)):
                if cur[i][j] == 'Q':
                    return False
            return True

        def solver(cur,r):
            if r == n:
                res.append(boardToList(cur))
                return
            for c in range(n):
                if canFit(r,c,cur):
                    cur[r][c] = 'Q'
                    solver(cur,r+1)
                    cur[r][c] = '.'
        solver(cur,0)
        return res