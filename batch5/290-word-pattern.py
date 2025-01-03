class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        p_to_s, s_to_p = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in p_to_s and p_to_s[pattern[i]] != s[i]:
                return False
            else:
                p_to_s[pattern[i]] = s[i]
            
            if s[i] in s_to_p and s_to_p[s[i]] != pattern[i]:
                return False
            else:
                s_to_p[s[i]] = pattern[i]
        
        return True
