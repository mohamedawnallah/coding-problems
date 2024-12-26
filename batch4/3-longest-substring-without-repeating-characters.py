class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = float('-inf')
        visited = set()
        window_start = 0
        for window_end in range(len(s)):
            while s[window_end] in visited:
                if s[window_start] == s[window_end]:
                    visited.remove(s[window_end])
                else:
                    visited.remove(s[window_start])
                window_start += 1

            max_len = max(max_len, window_end-window_start+1)
            visited.add(s[window_end])

        return max_len if max_len != float('-inf') else 0
