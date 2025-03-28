# 题目来源：https://leetcode.cn/problems/minimize-string-length/description/?envType=daily-question&envId=2025-03-28

# 方法一：哈希集合

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

# 方法二：位运算

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('a'))
        return mask.bit_count()
