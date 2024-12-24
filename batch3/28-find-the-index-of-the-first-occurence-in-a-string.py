class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length, needle_length = len(haystack), len(needle)
        if needle_length > haystack_length:
            return -1
        
        starting_positions = haystack_length - needle_length + 1
        for i in range(starting_positions):
            match_found = True
            for j in range(needle_length):
                if haystack[i+j] != needle[j]:
                    match_found = False
                    break
        
            if match_found:
                return i

        return -1
