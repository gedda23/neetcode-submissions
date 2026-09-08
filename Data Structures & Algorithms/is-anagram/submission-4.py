class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        else:
            for letter in s:
                seen[letter] = seen.get(letter,0)+1
            for letter in t:
                seen[letter] = seen.get(letter,0)-1
            return all(value ==0 for value in  seen.values())