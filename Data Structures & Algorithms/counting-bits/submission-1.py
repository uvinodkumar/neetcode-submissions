class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = [0] * (n+1)

        def num_of_ones (n):

            num_ones = 0

            while n:
                n = n & (n-1)
                num_ones += 1

            return num_ones

        # arr[0] = 0
        # arr[1] = 1

        for i in range( n+1):
            arr[i] = num_of_ones(i)

        return arr