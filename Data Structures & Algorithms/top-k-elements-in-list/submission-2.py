from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequencies
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Create buckets
        freq = [[] for i in range(len(nums) + 1)]

        # Step 3: Fill buckets
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 4: Traverse backwards
        res = []

        for i in range(len(freq)-1, 0, -1):

            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res