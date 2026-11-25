class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        base = 100003
        mod = 10**9 + 7

        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = (pow_base[i - 1] * base) % mod

        def has_unique(length: int) -> bool:
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            freq = defaultdict(int)
            freq[h] += 1

            for i in range(length, n):
                out_val = (nums[i - length] * pow_base[length - 1]) % mod
                h = (h - out_val + mod) % mod
                h = (h * base + nums[i]) % mod
                freq[h] += 1

            return any(count == 1 for count in freq.values())

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans