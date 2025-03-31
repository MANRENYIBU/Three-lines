# 题目来源：https://leetcode.cn/problems/percentage-of-letter-in-string/?envType=daily-question&envId=2025-03-31

# 方法一：遍历（模拟）

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        for c in s:
            if c == letter:
                cnt += 1
        return (cnt * 100) // len(s)


# 方法二：库函数

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
