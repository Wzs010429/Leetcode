# leetcode 37 解数独

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backTracking(board)

    def backTracking(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    continue
                for k in range(1, 10):
                    if self.isValid(board, i, j, k):
                        board[i][j] = str(k)
                        if self.backTracking(board):
                            return True
                        board[i][j] = "."
                return False
        return True

    def isValid(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == str(val):
                return False
            if board[i][col] == str(val):
                return False

        block_row = row // 3 * 3
        block_col = col // 3 * 3

        for i in range(block_row, block_row + 3):
            for j in range(block_col, block_col + 3):
                if board[i][j] == str(val):
                    return False

        return True