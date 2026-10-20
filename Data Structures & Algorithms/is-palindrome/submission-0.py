class Solution:
    def isPalindrome(self, s: str) -> bool:
        lIdx, rIdx = 0, len(s) - 1
        while lIdx < rIdx:
            while lIdx < rIdx and s[lIdx].isalnum() == False: lIdx += 1
            while lIdx < rIdx and s[rIdx].isalnum() == False: rIdx -= 1
            if s[lIdx].lower() != s[rIdx].lower(): return False
            lIdx += 1
            rIdx -= 1
        return True
        