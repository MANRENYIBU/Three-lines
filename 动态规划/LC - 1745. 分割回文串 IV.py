# 题目来源：https://leetcode.cn/problems/palindrome-partitioning-iv/description/

'''
在 1278. 分割回文串 III 中, 我们计算了分割字符串的最少修改次数; 
如果最少修改次数等于 0, 那么每段都是回文串; 
所以直接调用 1278 题的代码, 判断返回值是否为 0 即可; 
这样不仅能解决本题, 也能解决分成 4 段, 5 段, 更多段的问题; 
'''

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        min_change = []
        for _ in range(n):
            min_change.append([0] * n)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    min_change[i][j] = min_change[i + 1][j - 1] + 1
                else:
                    min_change[i][j] = min_change[i + 1][j - 1]

        f = min_change[0]
        for i in range(1, k):
            for r in range(n - k + i, i - 1, -1):
                ans = []
                for l in range(i, r + 1):
                    temp = f[l - 1] + min_change[l][r]
                    ans.append(temp)
                f[r] = min(ans)
        return f[-1]

    def checkPartitioning(self, s: str) -> bool:
        return self.palindromePartition(s, 3) == 0
