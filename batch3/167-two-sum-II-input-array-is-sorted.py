class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if s == "":
            return True

        ptr = 0
        for i in range(len(t)):
            if s[ptr] == t[i]:
                ptr += 1

            if ptr == len(s):
                return True

        return False
