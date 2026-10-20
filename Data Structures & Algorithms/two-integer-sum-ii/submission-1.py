class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lIdx, rIdx = 0, len(numbers) - 1
        while lIdx < rIdx:
            curr_sum = numbers[lIdx] + numbers[rIdx]
            if curr_sum == target: return [lIdx+1, rIdx+1]
            elif curr_sum < target: lIdx += 1
            else: rIdx -= 1
        return []
        