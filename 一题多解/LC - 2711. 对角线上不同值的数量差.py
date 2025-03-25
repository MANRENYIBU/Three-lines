# 题目来源：https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/?envType=daily-question&envId=2025-03-25

# 方法一：暴力计算

from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for _ in range(m):
            ans.append([0] * n)
        st = set()

        for i in range(m):
            for j in range(n):
                st.clear()
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    st.add(grid[x][y])
                    x -= 1
                    y -= 1
                top_left = len(st)

                st.clear()
                x, y = i + 1, j + 1
                while x < m and y < n:
                    st.add(grid[x][y])
                    x += 1
                    y += 1
                bottom_right = len(st)
                ans[i][j] = abs(top_left - bottom_right)
        return ans


# 方法二：前后缀分解

'''
对于同一条对角线, 方法一会多次遍历。
比如计算 ans[0][0] 的时候我们会遍历主对角线, 计算 ans[1][1] 的时候我们又会遍历主对角线。怎么减少遍历次数？

考察某一条对角线 d, 把它视作一个一维数组。对于 d[i] 来说：
topLeft 是在 d[i] 左边的不同元素个数。我们可以从左到右遍历 d, 同时把元素加到一个哈希集合中。
遍历到 d[i] 时, 哈希集合的大小就是 topLeft。
bottomRight 是在 d[i] 右边的不同元素个数。我们可以从右到左遍历 d, 同时把元素加到一个哈希集合中。
遍历到 d[i] 时, 哈希集合的大小就是 bottomRight。
'''

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        st = set()

        # 第一排在右上, 最后一排在左下
        # 每排从左上到右下
        # 令 k = i - j + n, 那么右上角 k = 1, 左下角 k = m + n - 1
        for k in range(1, m + n):
            # 核心：计算 j 的最小值和最大值
            min_j = max(n - k, 0) # i = 0 的时候, j = n - k, 但不能是负数
            max_j = min(m + n - 1 - k, n - 1)  # i = m - 1 的时候, j = m + n - 1 - k, 但不能超过 n - 1

            st.clear()
            for j in range(min_j, max_j + 1):
                i = k + j - n
                ans[i][j] = len(st)  # top_left[i][j] == len(st)
                st.add(grid[i][j])

            st.clear()
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - len(st))  # bottom_right[i][j] == len(st)
                st.add(grid[i][j])
        return ans


# 方法三：位运算优化

'''
本题值域范围为 [1,50], 我们可以用二进制数（64 位整数）记录哪些数字出现过。
遍历到 x=grid[i][j] 时, 方法二要加到集合中, 方法三改成把二进制数的从低到高第 x 位置为 1。
集合大小就是二进制数中的 1 的个数。
'''

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for k in range(1, m + n):
            min_j = max(n - k, 0)
            max_j = min(m + n - 1 - k, n - 1)

            st = 0
            for j in range(min_j, max_j + 1):
                i = k + j - n
                ans[i][j] = st.bit_count()  # 计算 st 中 1 的个数
                st |= 1 << grid[i][j]  # 把 grid[i][j] 加到 st 中

            st = 0
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - st.bit_count())
                st |= 1 << grid[i][j]
        return ans
