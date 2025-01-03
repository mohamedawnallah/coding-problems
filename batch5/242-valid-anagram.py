from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq, t_freq = Counter(s), Counter(t)
        for char in s:
            if char not in t_freq:
                return False

            if char in t_freq and t_freq[char] != s_freq[char]:
                return False
            
        for char in t:
            if char not in s_freq:
                return False

        return True
