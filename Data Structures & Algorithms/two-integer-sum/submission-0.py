class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, e in enumerate(nums):
            possible_match = target - e
            if possible_match in seen:
                return [seen[possible_match], i]
            seen[e] = i
        return []        
        