# Convert an Array Into 2D Array with Conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []

        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            count[n] += 1

        return res
