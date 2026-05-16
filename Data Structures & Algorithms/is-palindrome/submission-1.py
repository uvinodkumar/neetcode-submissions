class Solution:
    def isPalindrome(self, s: str) -> bool:

        # n = len(s)
        # left, right = 0, n-1

        # while left < right:

        #     if not s[left].isalnum():
        #         left = left + 1
        #         continue

        #     if not s[right].isalnum():
        #         right = right - 1
        #         continue
            
        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1
        #     right -= 1

        # return True

        new_s = ""

        for ch in s:
            if ch.isalnum():
                lower_ch = ch.lower()
                new_s += lower_ch

        return new_s == new_s[::-1]

        
        