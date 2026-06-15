class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count=Counter(nums)
        result=[y for y, freq in count.most_common(k)]
        return result
        