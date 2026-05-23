import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        final_dict = {}
        for element in nums:
            if element in seen:
                seen[element] += 1
            else:
                seen[element] = 1
        buckets = [[] for _ in range(len(nums)+1)]

        for key,value in seen.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1,0,-1):
            if buckets[i]:
                res.extend(buckets[i])
            if len(res)==k:
                return res
            





        