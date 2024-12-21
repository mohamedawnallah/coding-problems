class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if right != 0 and s[i] == " ":
                left = i+1
                break
            if right == 0 and s[i] != " ":
                right = i
        return right-left+1
