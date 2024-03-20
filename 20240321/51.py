# leetcode 51 N皇后

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessBorad = ["." * n] * n
        self.backTracking(n, 0, chessBorad, result)
        return result

    def backTracking(self, n, row, chessBorad, result):
        if row == n:
            result.append(chessBorad[:])
            return result

        for col in range(n):
            if self.isValid(row, col, chessBorad):
                chessBorad[row] = chessBorad[row][:col] + "Q" + chessBorad[row][col + 1:]
                self.backTracking(n, row + 1, chessBorad, result)
                chessBorad[row] = chessBorad[row][:col] + "." + chessBorad[row][col + 1:]

    def isValid(self, row, col, chessBorad):
        for i in range(row):
            if chessBorad[i][col] == "Q":
                return False

        i, j = row - 1, col + 1

        while i >= 0 and j < len(chessBorad[0]):
            if chessBorad[i][j] == "Q":
                return False
            i -= 1
            j += 1

        i, j = row - 1, col - 1

        while i >= 0 and j >= 0:
            if chessBorad[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        return True