class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining],i]
            seen[nums[i]] = i
        