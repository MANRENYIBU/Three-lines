# 题目来源：https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/description/

from functools import cache
class Solution:
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        '''
        i: 还剩下i条地毯
        j: 剩余砖块为floor[0]到floor[j], 即j + 1块砖
        dfs(i, j): 表示用i条地毯覆盖下标在[0, j]中的砖, 没被覆盖的白色砖块的最少数目

        状态定义与状态转移方程:
        考虑floor[j]是否覆盖:
        1. 不覆盖: 接下来要解决的问题是, 用i条地毯覆盖下标在[0, j - 1]中的砖, 没被覆盖的白色砖块的最少数目, 再加上int(floor[j])（刚好白色是1）, 得dfs(i,j) = dfs(i, j - 1) + int(floor[j])
        2. 覆盖: 接下来要解决的问题是, 用i - 1条地毯覆盖下标在[0,j - carpetLen]中的砖, 没被覆盖的白色砖块的最少数目, 即dfs(i, j)=dfs(i - 1, j - carpetLen)

        dfs(i,j) = min(dfs(i, j - 1) + int(floor[j]),dfs(i - 1, j - carpetLen)),
                or  dfs(i, j - 1) + int(floor[j]),

        递归边界: 如果j < carpetLen * i, 那么dfs(i, j) = 0, 因为剩余砖块可以全部覆盖
        递归入口: dfs(numCarpets, n - 1), 其中n是floor的长度; 这是原问题, 也是答案
        '''

        floor = list(map(int, floor))
        n = len(floor)
        @cache
        def dfs(i, j):
            if j < carpetLen * i: # 剩余砖块可以全部覆盖
                return 0
            if i == 0:
                return dfs(i, j - 1) + floor[j]
            return min(dfs(i, j - 1) + floor[j], dfs(i - 1, j - carpetLen))
        return dfs(numCarpets, n - 1)

