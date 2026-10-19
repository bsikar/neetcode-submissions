from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                element = board[rowIdx][colIdx]
                if element == '.': continue
                boxIdx = (rowIdx // 3, colIdx // 3)
                if (element in rows[rowIdx] or
                    element in cols[colIdx] or
                    element in boxes[boxIdx]): return False
                for s in (rows[rowIdx], cols[colIdx], boxes[boxIdx]): s.add(element)
        return True