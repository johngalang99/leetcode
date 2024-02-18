# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        candidate = min(height[l], height[r]) * (r - l)
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            candidate = max(candidate, water)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return candidate
