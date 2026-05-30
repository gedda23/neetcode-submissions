from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        
        res_lis = [[] for _ in range(len(nums)+1)]

        for key,value in seen.items():
            res_lis[value].append(key)
        
        res = []
        for num in range(len(res_lis)-1,0,-1):
            for value in res_lis[num]:
                res.append(value)
                if len(res) == k:
                    return res
        return []
