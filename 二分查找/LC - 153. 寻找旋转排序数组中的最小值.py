# 题目来源：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/1987499/by-endlesscheng-owgd/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (right + left) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]
