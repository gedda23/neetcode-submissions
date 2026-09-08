class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_result = [1]*len(nums)
        for idx in range(1,len(nums)):
            left_result[idx] = left_result[idx-1]*nums[idx-1]
        right_result = [1]*len(nums)
        for idx in range(len(nums)-2,-1,-1):
            right_result[idx] = right_result[idx+1]*nums[idx+1]
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = left_result[i] * right_result[i]
        return result


