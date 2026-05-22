class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0

        charSet = set()
        maxlen = 0

        for right in range(n):
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])

            length = right - left + 1
            if length > maxlen:
                maxlen = length

            # maxlen = max(maxlen, right - left + 1)

        return maxlen

                
        