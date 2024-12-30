class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def count_live_neighbors(x, y):
            count = 0
            for i in range(max(0, x-1), min(m, x+2)):
                for j in range(max(0, y-1), min(n, y+2)):
                    if (x, y) != (i, j) and abs(board[i][j]) == 1:
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors_count = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_neighbors_count < 2 or live_neighbors_count > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_neighbors_count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
        # Time Complexity: O(n * m)
        # Space Complexity: O(1)
