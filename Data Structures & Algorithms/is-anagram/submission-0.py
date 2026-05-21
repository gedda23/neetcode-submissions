class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in s_dict:
                    s_dict[i] = s_dict[i]+1
                else:
                    s_dict[i] = 1
            for j in t:
                if j in s_dict:
                    s_dict[j] = s_dict[j]-1
                else:
                    s_dict[j] = 1
        return all(value==0 for value in s_dict.values())

        