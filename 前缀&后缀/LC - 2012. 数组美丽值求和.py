# 题目来源：https://leetcode.cn/problems/sum-of-beauty-in-the-array/description/?envType=daily-question&envId=2025-03-11

'''
题目的这个要求, 相当于：

nums[i] 要大于 i 左边的所有数, 也就是大于前缀 [0, i - 1] 中的最大值。
nums[i] 要小于 i 右边的所有数, 也就是小于后缀 [i + 1, n - 1] 中的最小值。
这可以通过遍历算出来。

定义 sufMin[i] 表示后缀 [i,n - 1] 中的最小值。
那么 sufMin[i] 等于 nums[i] 与后缀 [i + 1, n - 1] 中的最小值, 二者取最小值, 即
sufMin[i] = min(nums[i], sufMin[i + 1])
注意上式需要从右到左遍历 nums 计算。

对于前缀最大值, 也同理。
我们可以在从左到右遍历 nums 的过程中, 维护前缀最大值 preMax。
注意这只需要一个变量, 因为我们可以一边计算 preMax, 一边计算答案。
'''

from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        suf_min = [0] * n  # 后缀最小值
        suf_min[n - 1] = nums[n - 1]
        for i in range(n - 2, 1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])

        ans = 0
        pre_max = nums[0]  # 前缀最大值
        for i in range(1, n - 1):
            x = nums[i]
            # 此时 pre_max 表示 [0, i-1] 中的最大值
            if pre_max < x < suf_min[i + 1]:
                ans += 2
            elif nums[i - 1] < x < nums[i + 1]:
                ans += 1
            # 更新后 pre_max 表示 [0, i] 中的最大值
            pre_max = max(pre_max, x)
        return ans
