class Solution:
    
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            step_cost = costs[i - 1] # 0-indexed access
            for jump in (1, 2, 3):
                if i - jump >= 0:
                    dp[i] = min(dp[i], dp[i - jump] + jump * jump + step_cost)
                    
        return dp[n]