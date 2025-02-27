# 题目来源：https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/

# 方法一：遍历

from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i > 0:
                pos += 1
        return max(pos, neg)

# 方法二：二分查找1

def lower_bound(nums: List[int], target: int)-> int:
    n = len(nums)
    left = 0
    right = n - 1  # 闭区间[left, right]
    while left <= right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid + 1, right]
        else:
            right = mid - 1  # [left, mid - 1]
    return left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = lower_bound(nums, 0)
        pos = n - lower_bound(nums, 1)
        return max(pos, neg)

# 方法二：二分查找2

from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)
