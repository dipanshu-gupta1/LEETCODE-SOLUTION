class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_p = lcm(*nums) * max(nums)

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if prod == l * g:
                    ans = max(ans, j - i + 1)

                if prod > max_p:
                    break

        return ans