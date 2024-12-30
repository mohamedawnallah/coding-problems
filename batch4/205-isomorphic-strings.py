class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check for the surjective property.
        if len(s) != len(t):
            return False

        s_to_t, t_to_s = {}, {}
        for i in range(len(s)):
            # Check if the domain element maps to different element in codomain.
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            else:
                s_to_t[s[i]] = t[i]
            
            # Check if the codomain element got mapped to once.
            if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False
            else:
                t_to_s[t[i]] = s[i]
            

        return True 
