class Solution:
    def minWindow(self, string: str, target: str) -> str:
        current_window_freq, target_freq = {}, {}
        for char in target:
            target_freq[char] = target_freq.get(char, 0) + 1
        
        window_start, window_end = 0, 0
        start, min_len = 0, float('inf')
        matches_required, matches_found = len(target_freq), 0
        while window_end < len(string):
            char = string[window_end]
            current_window_freq[char] = current_window_freq.get(char, 0) + 1
            if char in target_freq and current_window_freq[char] == target_freq[char]:
                matches_found += 1
            
            # Shrink the window.
            while matches_found == matches_required:
                # Compute the minimum window length.
                window_length = window_end - window_start + 1
                if window_length < min_len:
                    min_len = window_length
                    start = window_start
                
                char = string[window_start]
                current_window_freq[char] -= 1

                if char in target_freq and current_window_freq[char] < target_freq[char]:
                    matches_found -= 1

                window_start += 1

            window_end += 1

        print("start, min_len:", start, min_len)
        return string[start:start+min_len] if min_len != float('inf') else ""
