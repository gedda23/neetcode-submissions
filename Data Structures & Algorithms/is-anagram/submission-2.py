class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_dict = {}
        if len(s) != len(t):
            return False
        else:
            for char in s:
                seen_dict[char] = seen_dict.get(char,0)+1
            
            for char in t:
                seen_dict[char] = seen_dict.get(char,0)-1
        return all(value==0 for value in seen_dict.values())