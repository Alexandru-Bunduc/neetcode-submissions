class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        for i,line in enumerate(board):
            for j,val in enumerate(line):
             if val == ".": continue
             else:
                if line[j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in sqrs[(i//3)*3+(j//3)]:
                    return False
                rows[i].add(line[j])
                cols[j].add(board[i][j])
                sqrs[(i//3)*3+(j//3)].add(board[i][j])
        return True



