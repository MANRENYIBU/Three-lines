# 题目来源：https://leetcode.cn/problems/count-prefixes-of-a-given-string/description/?envType=daily-question&envId=2025-03-24

# 方法一：遍历

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for word in words:
            n = len(word)
            if word == s[:n]:
                cnt += 1
        return cnt
    
# 方法二：库函数

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)