class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        longest = 0
        for num in set_list:
            i=1
            length = 1
            while True:
                if num+i in set_list:
                    i = i+1
                    length = length+1
                    continue 
                else:
                    break
            longest = max(longest,length)
        return longest
            
            