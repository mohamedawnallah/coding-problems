class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for i in range(len(s)):
            if s[i] not in brackets:
                open_bracket = stack.pop() if stack else "#"
                if open_bracket not in brackets or brackets[open_bracket] != s[i]:
                    return False
            else:
                stack.append(s[i])

        return not stack
