class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = [1]*len(nums)
        right_list = [1]*len(nums)
        result_list = []
        for idx in range(1,len(nums)):
            left_list[idx] = left_list[idx-1]*nums[idx-1]
        
        for idx in range(len(nums)-2,-1,-1):
            right_list[idx] = right_list[idx+1]*nums[idx+1]
        for idx in range(len(nums)):
            result_list.append(left_list[idx]*right_list[idx])
        return result_list




