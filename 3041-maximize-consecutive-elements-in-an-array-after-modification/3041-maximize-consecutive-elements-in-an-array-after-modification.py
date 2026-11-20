class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        
        for x in nums:
            # Update x + 1 first so x isn't counted twice in the same step
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())