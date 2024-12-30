class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.flip_horizontally(matrix)
    

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def flip_horizontally(self, matrix):
        for i in range(len(matrix)):
            row = matrix[i]
            left, right = 0, len(row)-1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left, right = left+1, right-1
