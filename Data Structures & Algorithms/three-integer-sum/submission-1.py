class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triptlet_list = []
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums_sorted  = sorted(nums)
        for idx in range(len(nums_sorted)):
            fixed_num = nums_sorted[idx]
            remaining = 0-fixed_num
            left_pointer = idx+1
            right_pointer = len(nums)-1
            if idx <= len(nums_sorted)-3:
                while left_pointer < right_pointer:
                    sum_l = nums_sorted[left_pointer] + nums_sorted[right_pointer]
                    if sum_l == remaining:
                        if [fixed_num,nums_sorted[left_pointer],nums_sorted[right_pointer]] in triptlet_list:
                            pass
                        else:
                            triptlet_list.append([fixed_num,nums_sorted[left_pointer],nums_sorted[right_pointer]])
                        left_pointer += 1
                        right_pointer -= 1 
                    elif sum_l < remaining:
                        left_pointer += 1
                    else:
                        right_pointer -= 1
        return (triptlet_list)
