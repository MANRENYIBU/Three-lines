# 题目来源：https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import List

dirs = '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        path = [''] * n
        if n == 0:
            return []
        
        # 1
        path = [''] * n
        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return

            for c in dirs[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
        
        # 2
        path = []
        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            
            for c in dirs[int(digits[i])]:
                path.append(c)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return ans
