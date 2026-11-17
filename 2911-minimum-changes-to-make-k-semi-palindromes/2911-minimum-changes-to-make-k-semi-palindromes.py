class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Helper: min changes to make s[i..j] a semi-palindrome for a fixed divisor d
        def cost_with_divisor(i: int, j: int, d: int) -> int:
            changes = 0
            # Check each of the d groups
            for start in range(d):
                left = i + start
                right = j - ((j - i - start) % d)
                while left < right:
                    if s[left] != s[right]:
                        changes += 1
                    left += d
                    right -= d
            return changes

        # Precompute cost g[i][j] for every substring s[i..j] (0-indexed)
        g = [[float('inf')] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                m = length
                # Find all proper divisors of length m
                for d in range(1, m):
                    if m % d == 0:
                        g[i][j] = min(g[i][j], cost_with_divisor(i, j, d))

        # DP table: dp[i][j] = min changes to partition s[:i+1] into j parts
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            # Base case: 1 part from 0 to i
            dp[i][1] = g[0][i]
            
            # Fill for parts 2 to k
            for j in range(2, k + 1):
                for h in range(i):
                    if dp[h][j - 1] != float('inf') and g[h + 1][i] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[h][j - 1] + g[h + 1][i])

        return dp[n - 1][k]