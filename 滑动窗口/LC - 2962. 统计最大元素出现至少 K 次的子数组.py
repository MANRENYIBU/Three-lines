# 题目来源：https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/

'''
设 mx=max(nums);
右端点 right 从左到右遍历 nums; 遍历到元素 x=nums[right] 时, 如果 x=mx, 就把计数器 cntMx 加一;
如果此时 cntMx=k, 则不断右移左指针 left, 直到窗口内的 mx 的出现次数小于 k 为止;
此时, 对于右端点为 right 且左端点小于 left 的子数组, mx 的出现次数都至少为 k, 把答案增加 left
'''

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = left = cnt = 0
        for x in nums:
            if x == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
