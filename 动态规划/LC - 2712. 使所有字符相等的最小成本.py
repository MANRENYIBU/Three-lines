# 题目来源：https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal/description/?envType=daily-question&envId=2025-03-27

# 方法一：动态规划

from math import inf

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = inf
        suf = []
        for _ in range(n + 1):
            suf.append([0] * 2)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                suf[i][1] = suf[i + 1][1]
                suf[i][0] = suf[i + 1][1] + n - i
            else:
                suf[i][1] = suf[i + 1][0] + n - i
                suf[i][0] = suf[i + 1][0]
        
        pre = [0] * 2
        for i in range(n):
            if s[i] == '1':
                pre[0] = pre[1] + i + 1
            else:
                pre[1] = pre[0] + i + 1

        

            ans = min(ans, pre[0] + suf[i + 1][0], pre[1] + suf[i + 1][1])
        return ans


# 方法二：贪心

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i - 1] != s[i]:
                ans += min(i, n - i)
        return ans
