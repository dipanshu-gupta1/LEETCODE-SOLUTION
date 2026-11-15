class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix_sum = 0
        even_count = 1  # Base prefix sum of 0 is even
        odd_count = 0
        ans = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 1:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1

        return ans % MOD