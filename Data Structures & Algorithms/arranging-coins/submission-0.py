class Solution:
    def arrangeCoins(self, n: int) -> int:


        left = 1
        right = n
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2

            sum_till_mid = mid * (mid + 1) // 2

            if sum_till_mid == n:
                return mid
            elif sum_till_mid < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans