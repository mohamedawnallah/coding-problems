class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        left, right = -1, -1
        for i in range(len(s)-1, -1, -1):
            if right != -1 and s[i] == " ":
                left = i
                output += s[left+1:right+1] + " "
                right = -1

            if right == -1 and s[i] != " ":
                right = i
        
        if right != -1:
            output += s[:right+1]
        return output.strip()
