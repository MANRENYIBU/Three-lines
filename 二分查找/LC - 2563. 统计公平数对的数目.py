# 题目来源：https://leetcode.cn/problems/count-the-number-of-fair-pairs/

'''
枚举 nums[j]，那么 nums[i] 需要满足
lower - nums[j]≤nums[i]≤upper - nums[j]并且 0 ≤ i < j;
可以计算出 ≤ upper - nums[j] 的元素个数，减去 < lower - nums[j] 的元素个数，加入答案
'''
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            # 注意要在 [0, j) 中二分，因为题目要求两个下标 i < j
            r = bisect_right(nums, upper - x, 0, j)  # <= upper-nums[j] 的 nums[i] 的个数
            l = bisect_left(nums, lower - x, 0, j)  # < lower-nums[j] 的 nums[i] 的个数
            ans += r - l
        return ans
    

# 写法变化(手写二分)

from typing import List

def lower_bound(nums: List[int], target: int, left: int, right: int) -> int:
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            r = lower_bound(nums, upper - x + 1, 0, i)
            l = lower_bound(nums, lower - x, 0, i)
            ans += r - l
        return ans
