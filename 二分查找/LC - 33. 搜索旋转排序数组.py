# 题目来源：https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/1987503/by-endlesscheng-auuh/

# 方法一：二分查找-1

from typing import List

class Solution:
    # 153. 寻找旋转排序数组中的最小值（返回的是下标）
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return right

    # 有序数组中找 target 的下标
    def lower_bound(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            # 循环不变量：
            # nums[right] >= target
            # nums[left] < target
            if nums[mid] >= target:
                right = mid  # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        return right if nums[right] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        if target > nums[-1]:  # target 在第一段
            return self.lower_bound(nums, -1, i, target)  # 开区间 (-1, i)
        # target 在第二段
        return self.lower_bound(nums, i - 1, len(nums), target)  # 开区间 (i-1, n)


# 方法二：二分查找-2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i):
            end = nums[-1]
            if nums[i] > end:
                if target > end and nums[i] >= target:
                    return True
            else:
                if target > end or nums[i] >= target:
                    return True
        
        n = len(nums)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (right + left) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == n or nums[right] != target:
            return -1
        return right
