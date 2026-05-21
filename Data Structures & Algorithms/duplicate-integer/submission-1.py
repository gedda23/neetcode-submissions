class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
        # for idx in range(len(nums)-1):
        #     for duplicate in range(idx+1,len(nums)):
        #         if nums[idx] == nums[duplicate]:
        #             return True
        # return False


        