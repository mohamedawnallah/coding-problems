class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                grid_index = (i // 3) * 3 + (j // 3)

                # Check if the number has already been seen in the same row, column, or the grid.
                if num in rows[i] or num in cols[j] or num in grids[grid_index]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                grids[grid_index].add(num)
        
        return True
