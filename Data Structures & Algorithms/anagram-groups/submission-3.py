class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            sorted_string = "".join(sorted(st))
            if sorted_string not in seen:
                seen[sorted_string] = [st]
            else:
                seen[sorted_string].append(st)
        return list(seen.values())


        