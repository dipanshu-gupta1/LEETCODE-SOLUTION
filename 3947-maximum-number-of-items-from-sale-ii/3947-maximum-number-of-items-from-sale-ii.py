from collections import defaultdict
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        min_price = min(p for _, p in items)
        max_f = max(f for f, _ in items)

        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # Count how many items have a factor divisible by f
        multiples = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                total = 0
                for mult in range(f, max_f + 1, f):
                    total += freq[mult]
                multiples[f] = total

        # Collect 2-for-1 deals that are strictly cheaper than 2 * min_price
        deals = defaultdict(int)
        for f, price in items:
            cnt = multiples[f] - 1
            if cnt > 0 and price < 2 * min_price:
                deals[price] += cnt

        ans = 0
        for price in sorted(deals):
            take = min(deals[price], budget // price)
            ans += 2 * take
            budget -= take * price
            if budget == 0:
                break

        ans += budget // min_price
        return ans