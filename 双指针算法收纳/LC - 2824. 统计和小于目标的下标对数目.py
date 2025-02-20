# 题目来源：https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums, target):
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        cnt = 0
        while left < right:
            if nums[left] + nums[right] < target:
                cnt += right - left
                left += 1
            else:
                right -= 1
        return cnt
