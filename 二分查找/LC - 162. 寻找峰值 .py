# 题目来源：https://leetcode.cn/problems/find-peak-element/solutions/1987497/by-endlesscheng-9ass/

# 方法一：遍历

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] == max(nums):
            return 0
        if nums[-1] == max(nums):
            return n - 1
        for i in range(n):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# 方法二：二分查找

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (right + left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right
