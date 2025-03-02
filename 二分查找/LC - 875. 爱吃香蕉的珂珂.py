# 题目来源：https://leetcode.cn/problems/koko-eating-bananas/

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 0
        right = max(piles)
        while left + 1 < right:
            mid = (right + left) // 2
            s = 0
            for p in piles:
                s += (p - 1) // mid
            if s <= h - n:
                right = mid
            else:
                left = mid
        return right
