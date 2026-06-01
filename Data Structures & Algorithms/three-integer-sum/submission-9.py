class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triptlet_list = []
        nums_sorted  = sorted(nums)
        for idx in range(len(nums_sorted)):
            if idx <= len(nums_sorted)-3:
                if idx != 0:
                    if nums_sorted[idx] == nums_sorted[idx-1]:
                        continue
                fixed_num = nums_sorted[idx]
                remaining = 0-fixed_num
                left_pointer = idx+1
                right_pointer = len(nums)-1
                while left_pointer < right_pointer:
                    sum_l = nums_sorted[left_pointer] + nums_sorted[right_pointer]
                    if sum_l == remaining:
                        prev_left = nums_sorted[left_pointer]
                        prev_right = nums_sorted[right_pointer]
                        triptlet_list.append([fixed_num,nums_sorted[left_pointer],nums_sorted[right_pointer]])
                        left_pointer += 1
                        right_pointer -= 1
                        while (left_pointer < right_pointer) and (nums_sorted[left_pointer] == prev_left):
                            left_pointer += 1
                        while (left_pointer < right_pointer) and (nums_sorted[right_pointer] == prev_right):
                            right_pointer -= 1 

                    elif sum_l < remaining:

                        left_pointer += 1
                    else:
                        right_pointer -= 1
        return (triptlet_list)
