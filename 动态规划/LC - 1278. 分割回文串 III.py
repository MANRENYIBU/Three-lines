# 题目来源：https://leetcode.cn/problems/palindrome-partitioning-iii/description/

'''
我们需要在递归过程中跟踪以下信息: 

i: 还需要切 i 刀, 分出 i + 1 个子串。这样定义的目的是把 i = 0 用上, 后面 1:1 翻译成递推不浪费空间。
r: 剩余字符串的右端点为 r。
因此, 定义状态为 dfs(i, r), 表示把 s[0] 到 s[r] 划分成 i + 1 个非空子串, 每个子串修改成回文串, 总修改次数的最小值。
枚举最后一段子串的左端点 l = i,i+1,…,r, 那么接下来要解决的问题是; 
把 s[0] 到 s[l-1] 划分成 i 个非空子串, 每个子串修改成回文串, 总修改次数的最小值, 即 dfs(i - 1, l - 1)。
注意 l 最小是 i, 因为剩余的 i 个子串必须是非空的, 所以划分后的剩余长度至少是 i。
所有情况取最小值, 就得到了 dfs(i, r), 即
dfs(i,r)= min{dfs(i - 1, l - 1) + minChange(l, r)} i≤l≤r
其中 minChange 的定义见下文。

递归边界: dfs(0, r) = minChange(0, r)。此时只有一个子串。
递归入口: dfs(k-1, ∣s∣ - 1), 这是原问题, 也是答案。（∣s∣ 表示 s 的长度）

定义 minChange(i,j) 表示把子串 s[i] 到 s[j] 改成回文串, 至少要改多少个字母。
分类讨论：
如果 s[i] = s[j], 无需修改, 问题变成把 s[i+1] 到 s[j-1] 改成回文串, 至少要改多少个字母, 即 minChange(i, j) = minChange(i + 1, j - 1)。
如果 s[i] != s[j], 必须修改其中一个字母, 问题变成把 s[i+1] 到 s[j-1] 改成回文串, 至少要改多少个字母, 
即 minChange(i, j) = minChange(i + 1, j - 1) + 1。
所以有
minChange(i,j) = minChange(i + 1, j - 1)+[s[i] != s[j]]
其中 [s[i] != s[j]] 在 s[i] != s[j] 成立时为 1, 否则为 0。

递归边界：minChange(i, i) = minChange(i, i + 1)=0。如果子串只有一个字母, 或者子串是空串, 那么无需修改。
'''

from functools import lru_cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 把 s[i: j + 1] 改成回文串的最小修改次数
        @lru_cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def min_change(i: int, j: int) -> int:
            if i >= j:  # 子串只有一个字母，或者子串是空串
                return 0  # 无需修改
            return min_change(i + 1, j - 1) + (1 if s[i] != s[j] else 0)

        # 把 s[: r + 1] 切 i 刀，分成 i + 1 个子串，每个子串改成回文串的最小总修改次数
        @lru_cache
        def dfs(i: int, r: int) -> int:
            if i == 0:  # 只有一个子串
                return min_change(0, r)
            # 枚举子串左端点 l
            return min(dfs(i - 1, l - 1) + min_change(l, r)
                       for l in range(i, r + 1))

        return dfs(k - 1, len(s) - 1)


# 优化

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_change[i][j] = min_change[i + 1][j - 1] + (1 if s[i] != s[j] else 0)

        f = [[0] * n for _ in range(k)]
        f[0] = min_change[0]  # 无需 copy
        for i in range(1, k):
            for r in range(i, n - (k - 1 - i)):  # 右边还有 k − 1 − i 个子串
                f[i][r] = min(f[i - 1][l - 1] + min_change[l][r] for l in range(i, r + 1))
        return f[-1][-1]
