class Solution:
    def findSubstring(self, string: str, words: List[str]) -> List[int]:
        return self.find_substring_indices_sliding_window(string, words)

    def find_substring_indices_sliding_window(self, string, keys):
        result = []

        key_freqs = {}
        for key in keys:
            key_freqs[key] = key_freqs.get(key, 0) + 1
        
        keys_count, key_length = len(keys), len(keys[0])
        permutation_length = keys_count * key_length
        permutations_count = len(string) - permutation_length + 1
        for i in range(permutations_count):
            permutation = string[i:i+permutation_length]
            key_freqs_found = {}
            for j in range(0, len(permutation), key_length):
                key = permutation[j:j+key_length]
                key_freqs_found[key] = key_freqs_found.get(key, 0) + 1

            if key_freqs_found == key_freqs:
                result.append(i)
        
        return result

    def find_substring_indices_brute_force(self, string, keys):
        result = set()
        permutations = self.permute(keys)
        for permutation in permutations:
            key = "".join(permutation)
            index = string.find(key)
            while index != -1:
                if index not in result:
                    result.add(index)
                index = string.find(key, index+1)
        return list(result)


    def permute(self, words):
        def backtrack(current_permutation, words):
            if not words:
                result.append(current_permutation[:])
                return
            for i in range(len(words)):
                current_permutation.append(words[i])
                backtrack(current_permutation, words[:i]+words[i+1:])
                current_permutation.pop()
        
        result = []
        backtrack([], words)
        return result
