class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [0] * (2*n) 

        for i in range(n):
            result[i] = nums[i]
        for i in range(n, 2*n):
            result[i] = nums[i - n]

        return result
