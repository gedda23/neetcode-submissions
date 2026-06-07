class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            max_len = 1
            for i in range(len(s)):
                substring = {s[i]}
                for j in range(i+1,len(s)):
                    if s[j] in substring:
                        break
                    else:
                        substring.add(s[j])
                        max_len = max(max_len,len(substring))
            return max_len
        