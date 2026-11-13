class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Deque stores [value, count] in strictly increasing order of value
        dq = deque()
        curr_ops = 0
        ans = 0
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            curr_count = 1
            # Flatten all smaller/equal blocks to the right up to nums[l]
            while dq and dq[0][0] <= nums[l]:
                val, cnt = dq.popleft()
                curr_ops += (nums[l] - val) * cnt
                curr_count += cnt
            dq.appendleft([nums[l], curr_count])
            
            # Shrink from the right if total operations exceed k
            while curr_ops > k:
                curr_ops -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            ans += (r - l + 1)
            
        return ans
        