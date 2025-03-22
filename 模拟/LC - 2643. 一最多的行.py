# 题目来源：https://leetcode.cn/problems/row-with-maximum-ones/description/?envType=daily-question&envId=2025-03-22

from typing import List
from math import inf

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = cnt = float(-inf)
        for i, row in enumerate(mat):
            s = 0
            for j in row:
                if j == 1:
                    s += 1
            if s > cnt:
                idx = i
                cnt = s
        return [idx, cnt]
