# 题目来源：https://leetcode.cn/problems/trapping-rain-water/

# 题目来源；https://leetcode.cn/problems/trapping-rain-water/description/

# 解法一：前后缀分解
class Solution:
    def trap(self, height):
        n = len(height)
        pre_max = [0] * n  # 前缀最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        
        sur_max = [0] * n  # 后缀最大值
        sur_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            sur_max[i] = max(sur_max[i + 1], height[i])

        ans = 0
        for h, pre, sur in zip(height, pre_max, sur_max):
            ans += min(pre, sur) - h
        return ans


# 解法二：相向双指针
class Solution:
    def trap(self, height):
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
