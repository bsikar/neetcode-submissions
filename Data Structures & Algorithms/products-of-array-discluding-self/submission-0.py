class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len < 1: return []
        max_product = 1
        num_zero = 0
        for e in nums:
            if e != 0: max_product *= e
            else: num_zero += 1
        output = [0] * nums_len
        for i in range(nums_len):
            if num_zero == 1 and nums[i] == 0:
                # hit the only 0
                output[i] = max_product
            elif num_zero > 0:
                output[i] = 0
            else:
                output[i] = max_product // nums[i]
        return output
