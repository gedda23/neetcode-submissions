class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        longest = 0
        for num in set_list:
            if num-1 not in set_list:
                length = 1
                while num+length in set_list:
                    length = length+1
                longest = max(longest,length)
        return longest
            
            