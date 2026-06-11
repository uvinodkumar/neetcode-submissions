class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left_s = 0
        count = len(s)

        if count == 0:
            return True

        for right in range(len(t)):

            if s[left_s] == t[right]:
                left_s += 1
                count -= 1
            else:
                continue
            
            if count == 0:
                return True
        
        return False
