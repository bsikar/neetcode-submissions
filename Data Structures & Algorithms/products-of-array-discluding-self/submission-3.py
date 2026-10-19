class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        running_product = 1
        for e in nums:
            output.append(running_product)
            running_product *= e
        running_product = 1
        for i in reversed(range(len(nums))):
            output[i] *= running_product
            running_product *= nums[i]

        return output
        
