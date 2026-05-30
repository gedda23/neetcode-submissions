class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for idx in range(1,len(nums)):
            result[idx] = result[idx-1]*nums[idx-1]
        
        right_product = 1
        for idx in range(len(nums)-1,-1,-1):
            result[idx] = result[idx]*right_product
            right_product = right_product*nums[idx]

        return result     




