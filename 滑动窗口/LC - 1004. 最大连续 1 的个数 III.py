# 题目来源：https://leetcode.cn/problems/max-consecutive-ones-iii/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = left = cnt0 = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > k:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
