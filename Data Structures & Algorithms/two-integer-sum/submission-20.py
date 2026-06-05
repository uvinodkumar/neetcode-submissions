class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = [0,0]

        i = 0
        ind = {}
        
        for num in nums:

            if target - num in ind:
                result[0] = ind[target-num]
                result[1] = i

                return result
            
            else:

                ind[num] = i

            i += 1

