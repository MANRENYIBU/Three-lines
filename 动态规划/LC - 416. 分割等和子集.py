# 题目来源：https://leetcode.cn/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07

'''
定义 dfs(i,j) 表示能否从 nums[0] 到 nums[i] 中选出一个和恰好等于 j 的子序列。

考虑 nums[i] 选或不选：
选：问题变成能否从 nums[0] 到 nums[i - 1] 中选出一个和恰好等于 j - nums[i] 的子序列, 即 dfs(i - 1,j - nums[i])。
不选：问题变成能否从 nums[0] 到 nums[i - 1] 中选出一个和恰好等于 j 的子序列, 即 dfs(i - 1,j)。
这两个只要有一个成立, dfs(i,j) 就是 true。

所以有：
dfs(i,j)=dfs(i - 1,j - nums[i]) || dfs(i - 1,j)
代码实现时, 可以只在 j≥nums[i] 时才调用 dfs(i - 1,j - nums[i]), 因为任何子序列的和都不会是负的。

递归边界：dfs( - 1,0)=true, dfs(-1, >0)=false。
递归入口：dfs(n - 1,s/2), 即答案。
'''

from typing import List
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
    
        @cache
        def dfs(i, j):
            if i < 0:
                return j == 0
            return dfs(i - 1, j) or (j >= nums[i] and dfs(i - 1, j - nums[i]))
        
        if s % 2:
            return False
        else:
            return dfs(n - 1, s // 2)
        
# 翻译为递归

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2:
            return False
        s //= 2  # 注意这里把 s 减半了
        f = [[False] * (s + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for j in range(s + 1):
                f[i + 1][j] = j >= x and f[i][j - x] or f[i][j]
        return f[n][s]
