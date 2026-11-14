class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')

        for k in range(l,r+1):
            window_sum = sum(nums[:k])
            if window_sum > 0 :
                min_sum = min(window_sum , min_sum)

            for i in range(k,len(nums)):
                window_sum += nums[i] - nums[i-k]
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)
        return -1 if min_sum == float('inf') else min_sum