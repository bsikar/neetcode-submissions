class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_as_set = set(nums)
        output = 0
        for e in nums_as_set:
            if e + 1 in nums_as_set: continue
            cnt = 1
            while e - cnt in nums_as_set: cnt += 1
            if cnt > output: output = cnt
        return output
