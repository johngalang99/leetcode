# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = length of longest common subsequence
        # between text1[:i] and text2[:j]
        dp = [
            [0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)
        ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[i + 1][j + 1] = (
                    (dp[i][j] + 1)
                    if text1[i] == text2[j]
                    else max(dp[i + 1][j], dp[i][j + 1])
                )
        return dp[-1][-1]
