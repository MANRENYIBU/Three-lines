# 题目来源：https://leetcode.cn/problems/container-with-most-water/
class Solution:
    def maxArea(self, height):
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
