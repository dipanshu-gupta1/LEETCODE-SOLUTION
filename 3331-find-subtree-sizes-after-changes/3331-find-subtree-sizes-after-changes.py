from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_children = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26

        # Pass 1: Find the closest ancestor with the same character for each node
        def assign_parents(u: int) -> None:
            c = ord(s[u]) - ord('a')
            if last_seen[c] != -1:
                new_parent[u] = last_seen[c]

            prev = last_seen[c]
            last_seen[c] = u

            for v in orig_children[u]:
                assign_parents(v)

            last_seen[c] = prev

        assign_parents(0)

        # Build adjacency list for the updated tree
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        # Pass 2: Compute subtree sizes in the updated tree
        def calc_size(u: int) -> int:
            total = 1
            for v in new_children[u]:
                total += calc_size(v)
            ans[u] = total
            return total

        calc_size(0)
        return ans