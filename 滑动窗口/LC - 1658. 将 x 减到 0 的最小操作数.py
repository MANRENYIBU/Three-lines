# 题目来源：https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        aim = sum(nums) - x
        if aim < 0:
            return -1
        
        ans = -1
        left = s = 0
        n = len(nums)
        for right, x in enumerate(nums):
            s += x
            while s > aim:
                s -= nums[left]
                left += 1
            if s == aim:
                ans = max(ans, right - left + 1)
        if ans < 0:
            return -1
        else:
            return n - ans
