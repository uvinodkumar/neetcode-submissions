class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = [0] * 2

        ind = {}

        i = 0

        for num in nums:
            if target - num in ind:
                result[0] = ind[target - num]
                result[1] = i

                return result
            else:
                ind[num] = i

            i += 1

        