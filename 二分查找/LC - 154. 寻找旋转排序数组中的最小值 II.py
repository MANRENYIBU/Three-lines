# 题目来源：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/

'''
本题与 153 题的区别是有相同元素, 这会导致在二分查找时, 可能会遇到恰好二分元素 nums[mid] 与数组末尾元素 nums[n - 1] 相同的情况, 此时无法确定答案在左半区间中还是右半区间中; 
既然无法确定最小值所在区间, 那么干脆去掉 nums 的最后一个数, 继续二分; 换句话说, 此时问题变成了一个规模为 n - 1 的子问题; 
你可能会有疑问: 这会不会碰巧去掉了最小值？
这是不会的: 

如果去掉的数是最小值, 那么 nums[mid] 也是最小值, 这说明最小值仍然在数组中; 
如果去掉的数不是最小值, 那么我们排除了一个错误答案; 
为了方便写代码, 我们可以把 right 当作「数组最后一个数的下标」: 

如果 nums[mid]=nums[right], 那么和上面一样, 去掉 nums[right], 也就是把 right 减一; 
如果 nums[mid]<nums[right], 那么下标大于 mid 的数都在最小值的右边, 都可以去掉, 也就是把 right 更新为 mid; 
如果 nums[mid]>nums[right], 和 153 题一样, 把 left 更新为 mid; 
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (right + left) // 2
            if nums[mid] == nums[right]:  # 去掉 nums[right]
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return nums[right]
