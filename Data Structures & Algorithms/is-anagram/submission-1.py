class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def frequency(s):

            freq = {}

            for ch in s:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
            
            return freq

        return frequency(s) == frequency(t)
        