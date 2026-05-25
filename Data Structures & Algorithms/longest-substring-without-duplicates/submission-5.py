class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        charSet = set()
        count = 0
        maxcount = 0
        left = 0

        for right in range(n):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])

            maxcount = max(right - left + 1, maxcount)

        return maxcount
