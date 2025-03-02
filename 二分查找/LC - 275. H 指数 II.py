# 题目来源：https://leetcode.cn/problems/h-index-ii/

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 在区间 [left, right] 内询问
        left = 1
        right = len(citations)
        while left <= right:  # 区间不为空
            # 循环不变量：
            # left-1 的回答一定为「是」
            # right+1 的回答一定为「否」
            mid = (left + right) // 2
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid + 1  # 询问范围缩小到 [mid+1, right]
            else:
                right = mid - 1  # 询问范围缩小到 [left, mid-1]
        # 循环结束后 right 等于 left-1，回答一定为「是」
        # 根据循环不变量，right 现在是最大的回答为「是」的数
        return right
