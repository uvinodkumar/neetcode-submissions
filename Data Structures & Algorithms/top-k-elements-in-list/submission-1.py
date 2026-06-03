class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        res = [(value,key) for key, value in freq.items()]
        res.sort(reverse=True)

        for i in range(k):
            ans.append(res[i][1])
        
        return ans
        