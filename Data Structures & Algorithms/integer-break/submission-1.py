class Solution:

    def integerBreak(self, n: int) -> int:
        # dp[i] will store the maximum product for sum i
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                # For a split (j, i - j), we can either:
                # 1. Not split (i - j) further -> j * (i - j)
                # 2. Split (i - j) further -> j * dp[i - j]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]