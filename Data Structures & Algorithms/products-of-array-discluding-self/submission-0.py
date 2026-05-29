class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        output = []
        for idx1,num in enumerate(nums,start=0):
            multiplication = 1
            for idx2, j in enumerate(nums,start=0):
                if idx1 != idx2:
                    multiplication = multiplication*j
            output.append(multiplication)
        return output