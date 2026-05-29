class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = list(set(nums))
        global_max_length = 0
        for num in set_list:
            i=1
            max_length = 1
            while True:
                if num+i in set_list:
                    i = i+1
                    max_length = max_length+1
                    continue 
                else:
                    break
            global_max_length = max(global_max_length,max_length)
        return global_max_length
            
            