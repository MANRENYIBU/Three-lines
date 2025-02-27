# 题目来源：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# 方法一：暴力遍历
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                j = i + 1
                while j < n and nums[j] == target:
                    j += 1
                return [i, j - 1]
        return [-1, -1]

# 方法一：二分查找
'''
要求 nums 是非递减的，即 nums[i]<= nums[i +1]
返回最小的满足 nums[i] >= target 的 i
如果不存在，返回 len(nums)
'''
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

def lower_bound2(nums: List[int], target: int)-> int:
    n = len(nums)
    left = 0
    right = n  # 左闭右开区间[left, right)
    while left < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid + 1, right)
        else:
            right = mid  # [left, mid)
    return left  # right

def lower_bound3(nums: List[int], target: int)-> int:
    n = len(nums)
    left = -1
    right = n  # 开区间(left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid  # (mid, right)
        else:
            right = mid  # (left, mid)
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = lower_bound(nums, target)
        if start == n or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
