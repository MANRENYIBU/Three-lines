# 题目来源：https://leetcode.cn/problems/find-the-k-beauty-of-a-number/description/?envType=daily-question&envId=2025-03-10

# 方法一：字符串

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(k, len(s) + 1):
            x = int(s[i - k: i])
            if x > 0 and num % x == 0:
                ans += 1
        return ans


# 方法二：数学

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = 10 ** k
        cnt = 0
        m = num
        while m >= n // 10:
            x = m % n
            if x > 0 and num % x == 0:
                cnt += 1
            m //= 10
        return cnt
