# 题目来源：https://leetcode.cn/problems/find-a-peak-element-ii/

# 方法一：暴力

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(m):
            for j in range(n):
                flag = True
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if mat[x][y] > mat[i][j]:
                        flag = False
                        break
                if flag:
                    return [i, j]
        return [0, 0]


# 方法二：二分

'''
如果 mat[i] 的最大值比它下面的相邻数字小, 则存在一个峰顶, 其行号大于 i; 
缩小二分范围, 更新二分区间左端点 left; 
如果 mat[i] 的最大值比它下面的相邻数字大, 则存在一个峰顶, 其行号小于或等于 i; 
缩小二分范围, 更新二分区间右端点 right; 
'''


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (right + left) // 2
            mx = max(mat[mid])
            if mx > mat[mid + 1][mat[mid].index(mx)]:
                right = mid
            else:
                left = mid
        return [right, mat[right].index(max(mat[right]))] 
