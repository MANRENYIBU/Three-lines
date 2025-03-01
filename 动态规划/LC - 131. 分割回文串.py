# 题目来源：https://leetcode.cn/problems/palindrome-partitioning/description/

# 方法一：输入的视角（逗号选或不选）
'''
假设每对相邻字符之间有个逗号，那么就看每个逗号是选还是不选
也可以理解成：是否要把 s[i] 当成分割出的子串的最后一个字符。注意 s[n - 1] 一定是最后一个字符，一定要选
'''

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:
                ans.append(path.copy())  # 复制 path
                return

            # 不选 i 和 i+1 之间的逗号（i = n-1 时一定要选）
            if i < n - 1:
                dfs(i + 1, start)

            # 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                dfs(i + 1, i + 1)  # 下一个子串从 i+1 开始
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans

# 方法二：答案的视角（枚举子串结束位置）

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  # 复制 path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]
                if t == t[::-1]:  # 判断是否回文
                    path.append(t)
                    dfs(j + 1)
                    path.pop()  # 恢复现场

        dfs(0)
        return ans
