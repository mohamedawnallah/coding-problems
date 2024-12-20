class Solution:
    def candy(self, ratings: List[int]) -> int:
        distributions = [1] * len(ratings)

        # Left Distribution
        n = len(distributions)
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                distributions[i] = distributions[i-1]+1
        
        # Right Distributions
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                distributions[i] = max(distributions[i], distributions[i+1]+1)

        return sum(distributions)
