# top k frequencies

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        top_keys = [key for key, _ in counter.most_common(k)]

        return top_keys
        