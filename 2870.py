# /minimum-number-of-operations-to-make-array-empty/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for value in count.values():
            if value == 1:
                return -1

            res += math.ceil(value/3)

        return res
