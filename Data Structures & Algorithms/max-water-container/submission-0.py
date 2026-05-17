class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        maxarea = 0

        left, right = 0, n - 1

        while left < right:

            length = right - left
            breadth = min(heights[left], heights[right])

            area = length * breadth

            maxarea = max(maxarea, area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return maxarea
        

        