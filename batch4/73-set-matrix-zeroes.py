class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, columns = set(), set()
        
        # Initialize the unique indices for both rows and zeros where zero values happen.
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.add(i)
                    if j not in columns:
                        columns.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0   
