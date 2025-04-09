# 题目来源：https://leetcode.cn/problems/minimum-operations-to-make-array-values-equal-to-k/?envType=daily-question&envId=2025-04-09

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        n = len(set(nums))
        if k > mn:
            return -1
        return n - (mn == k)
