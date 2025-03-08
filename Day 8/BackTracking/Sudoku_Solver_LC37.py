import heapq
from typing import List

def solveSudoku(self, board: List[List[str]]) -> None:
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        empty = []

        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val == '.':
                    empty.append((i,j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i//3][j//3].add(val)
        empty = [
            (9 - len(rows[i] | cols[j] | boxes[i//3][j//3]),i,j)
            for i,j in empty
        ]

        heapq.heapify(empty)

        def fillBoard():
            if not empty:
                return True
            _,i,j = heapq.heappop(empty)
            row = rows[i]
            col = cols[j]
            box = boxes[i//3][j//3]
            nums = 0
            for val in '123456789':
                if (val in row or val in col or val in box):
                    continue
                board[i][j] = val
                row.add(val)
                col.add(val)
                box.add(val)
                if fillBoard():
                    return True
                row.remove(val)
                col.remove(val)
                box.remove(val)
                nums += 1
            heapq.heappush(empty,(nums,i,j))
            return False
        fillBoard()