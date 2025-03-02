# 题目来源：https://leetcode.cn/problems/minimize-maximum-of-array/

'''
「最小化最大值」就是二分答案的代名词; 我们猜测一个上界 limit, 即要求操作后所有元素均不超过 limit;
由于 limit 越大越能够满足, 越小越无法满足, 有单调性, 可以二分答案; 
从后往前模拟: 如果 nums[i]>limit, 那么应当去掉多余的 extra=nums[i] - limit 加到 nums[i - 1] 上, 最后如果 nums[0] ≤ limit, 则二分判定成功; 
代码实现时可以不用修改 nums, 而是维护 extra 变量; 

细节:
开区间二分下界: min(nums) - 1, 无法操作; 也可以简单地写成 -1
开区间二分上界: max(nums), 一定可以操作
'''

from typing import List
from bisect import bisect_left

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                extra = max(nums[i] + extra - limit, 0)
            return nums[0] + extra <= limit
        return bisect_left(range(max(nums)), True, lo=min(nums), key=check)
