# 题目来源：https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/

'''
移动右指针 right, 并统计相邻相同的情况出现了多少次, 记作 same;
如果 same>1, 则不断移动左指针 left 直到 s[left]=s[left - 1], 此时将一对相同的字符移到窗口之外。然后将 same 置为 1;
然后统计子串长度 right - left + 1 的最大值
'''

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        left = same = 0
        n = len(s)
        for right in range(1, n):
            if s[right] == s[right - 1]:
                same += 1
            if same > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                same = 1
            ans = max(ans, right - left + 1)
        return ans
