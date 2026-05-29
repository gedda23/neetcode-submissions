class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        longest = 0
        for num in set_list:
            length = 1
            current = num
            while current+1 in set_list:
                current = current+1
                length = length+1
            longest = max(longest,length)
        return longest
            
            