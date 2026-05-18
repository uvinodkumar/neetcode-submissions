class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        pairs = [(count, key) for key, count in freq.items()]
        pairs.sort(reverse = True)

        result = []

        for i in range(k):
            result.append(pairs[i][1])

        return result