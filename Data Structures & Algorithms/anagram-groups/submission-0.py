from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i, s in enumerate(strs):
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())      