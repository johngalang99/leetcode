# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            if (nums[r-1] != nums[r]):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l