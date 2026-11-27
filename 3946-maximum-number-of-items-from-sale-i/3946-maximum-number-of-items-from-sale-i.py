from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1

        # Precompute total copies gained on first purchase for each unique factor
        gain_by_factor = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                total = 0
                for mult in range(f, max_factor + 1, f):
                    total += freq[mult]
                gain_by_factor[f] = total

        # 0/1 Knapsack for first-time purchases
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for f, price in items:
            if price < min_price:
                min_price = price
            gain = gain_by_factor[f]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain > dp[b]:
                    dp[b] = dp[b - price] + gain

        # Spend any remaining budget on the cheapest item
        ans = 0
        for b in range(budget + 1):
            total_copies = dp[b] + (budget - b) // min_price
            if total_copies > ans:
                ans = total_copies

        return ans