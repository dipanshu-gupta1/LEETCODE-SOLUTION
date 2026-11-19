

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        change_two_min = nums[-1] - nums[2]
        change_both_ends = nums[-2] - nums[1]
        change_two_max = nums[-3] - nums[0]
        
        return min(change_two_min, change_both_ends, change_two_max)