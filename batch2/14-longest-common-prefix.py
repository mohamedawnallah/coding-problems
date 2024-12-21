class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            string = strs[i]
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
