class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]

        # result = [0] * 2

        # ind = {}

        # i = 0

        # for num in nums:
        #     if target - num in ind:
        #         result[0] = ind[target - num]
        #         result[1] = i
        #         return result
        #     else:
        #         ind[num] = i
        #     i = i + 1
