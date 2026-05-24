from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+count.get(num,0)
        bucket = [[] for _ in range(len(nums)+1)]
        for key,value in count.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

