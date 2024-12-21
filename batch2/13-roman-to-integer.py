class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for i in range(len(s)):
            current_value = roman_to_int[s[i]]
            if i < len(s)-1 and current_value < roman_to_int[s[i+1]]:
                result -= current_value
            else:
                result += current_value
        return result
