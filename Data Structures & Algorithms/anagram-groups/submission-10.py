class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            idx_list = [0]*26
            for char in word:
                idx = ord(char)-ord('a')
                idx_list[idx] = idx_list[idx] + 1
            anagram_dict[tuple(idx_list)].append(word)
        return [lis for lis in anagram_dict.values()] 


             
