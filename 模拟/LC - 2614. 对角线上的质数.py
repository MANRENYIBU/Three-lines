# 题目来源：https://leetcode.cn/problems/prime-in-diagonal/description/?envType=daily-question&envId=2025-03-18

'''
思路:
遍历两条对角线上的元素，如果是质数则更新答案的最大值。
注意 1 不是质数。
'''

from typing import List
from math import isqrt

class Solution:
    def is_prime(self, num):
        if num == 1:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(nums):
            for j in row[i], row[-i - 1]:
                if j > ans and self.is_prime(j):
                    ans = j
        return ans
