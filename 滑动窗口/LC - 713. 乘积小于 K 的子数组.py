# 题目来源：https://leetcode.cn/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right, x in enumerate(nums):  # x = nums[right]
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
