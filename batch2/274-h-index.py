class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex = 0
        for i in range(len(citations)):
            if citations[i] < i+1:
                break
            hindex += 1
        return hindex
