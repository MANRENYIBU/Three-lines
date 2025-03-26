# 题目来源：https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/?envType=daily-question&envId=2025-03-26

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        pre = min( k // 2, n)
        ans = pre * (pre + 1)(2 * k + n - pre - 1)(n - pre) // 2
        return ans
