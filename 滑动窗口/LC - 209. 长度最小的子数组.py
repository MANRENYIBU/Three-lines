# 题目来源：https://leetcode.cn/problems/minimum-size-subarray-sum/description/

from math import inf
class Solution:
    def minSubArrayLen(self, target, nums):
        ans = inf
        n = len(nums)
        s = 0
        left = 0
        for right, x in enumerate(nums):  # x = nums[right]
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        if ans <= n:
            return ans
        else:
            return 0
