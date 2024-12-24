class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        matrix = [[] for _ in range(numRows)]
        row, down = 0, True
        for char in s:
            matrix[row].append(char)
            if down:
                row += 1
                if row == numRows:
                    row -= 2
                    down = False
            else:
                row -= 1
                if row == -1:
                    row += 2
                    down = True

        result = ""
        for row in matrix:
            result += "".join(row)
        return result
