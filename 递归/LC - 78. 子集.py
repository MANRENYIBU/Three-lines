# 题目来源：https://leetcode.cn/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        # 1
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            dfs(i + 1)

            x = nums[i]
            path.append(x)
            dfs(i + 1)
            path.pop()
        
        # 2
        def dfs(i):
            ans.append(path.copy())

            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        
        dfs(0)
        return ans
