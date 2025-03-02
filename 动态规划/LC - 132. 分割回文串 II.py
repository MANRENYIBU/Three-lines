# 题目来源：https://leetcode.cn/problems/palindrome-partitioning-ii/description/

from functools import lru_cache
from math import inf

class Solution:
    def minCut(self, s: str) -> int:
        # 返回 s[l:r+1] 是否为回文串
        @lru_cache  # 缓存装饰器，避免重复计算 is_palindrome（一行代码实现记忆化）
        def is_palindrome(l: int, r: int) -> bool:
            if l >= r:
                return True
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        @lru_cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(r: int) -> int:
            if is_palindrome(0, r):  # 已是回文串，无需分割
                return 0
            res = inf
            for l in range(1, r + 1):  # 枚举分割位置
                if is_palindrome(l, r):
                    res = min(res, dfs(l - 1) + 1)  # 在 l-1 和 l 之间切一刀
            return res

        return dfs(len(s) - 1)


# 优化

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # is_palindrome[l][r] 表示 s[l:r+1] 是否为回文串
        is_palindrome = [[True] * n for _ in range(n)]
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                is_palindrome[l][r] = s[l] == s[r] and is_palindrome[l + 1][r - 1]

        f = [0] * n
        for r, is_pal in enumerate(is_palindrome[0]):
            if is_pal:  # 已是回文串，无需分割
                continue
            res = inf
            for l in range(1, r + 1):  # 枚举分割位置
                if is_palindrome[l][r]:
                    res = min(res, f[l - 1] + 1)  # 在 l-1 和 l 之间切一刀
            f[r] = res
        return f[-1]
