# 题目来源：https://leetcode.cn/problems/minimum-reverse-operations/description/?envType=daily-question&envId=2025-03-20

# 方法一：BFS + 有序集合

'''
由于等差数列的公差为 2，翻转后的下标要么都是偶数，要么都是奇数。
我们用两个有序集合 indices0和 indices1分别维护没有访问过的偶数下标和奇数下标。
注意这些下标不能在 banned 中。由于 p 是起点（已访问），所以也不在有序集合中。然后用 BFS 模拟。
在有序集合上，一边遍历翻转后的下标 j，一边把 j 从有序集合中删除。这样可以避免重复访问已经访问过的下标，也方便我们查找下一个没有访问过的下标。
'''

from sortedcontainers import SortedList
from collections import deque
from typing import List

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban = set(banned) | {p}
        indices = [SortedList(), SortedList()]  # import sortedcontainers
        for i in range(n):
            if i not in ban:
                indices[i % 2].add(i)
        indices[0].add(n)  # 哨兵，下面无需判断越界
        indices[1].add(n)

        ans = [-1] * n
        ans[p] = 0  # 起点
        q = deque([p])
        while q:
            i = q.popleft()
            # indices[mn % 2] 中的从 mn 到 mx 的所有下标都可以从 i 翻转到
            mn = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, n * 2 - k - i - 1)
            sl = indices[mn % 2]
            idx = sl.bisect_left(mn)
            while sl[idx] <= mx:
                j = sl.pop(idx)  # 注意 pop(idx) 会使后续元素向左移，不需要写 idx += 1
                ans[j] = ans[i] + 1  # 移动一步
                q.append(j)
        return ans


# 方法二：BFS + 并查集

class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def merge(self, from_: int, to: int) -> None:
        self.fa[self.find(from_)] = self.find(to)

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        indices = UnionFind(n + 2)
        indices.merge(p, p + 2)  # 删除 p
        for i in banned:
            indices.merge(i, i + 2)  # 删除 i

        ans = [-1] * n
        ans[p] = 0
        q = deque([p])
        while q:
            i = q.popleft()
            mn = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, n * 2 - k - i - 1)
            j = indices.find(mn)
            while j <= mx:
                ans[j] = ans[i] + 1
                q.append(j)
                indices.merge(j, mx + 2)  # 删除 j
                j = indices.find(j + 2)  # 快速跳到 >= j+2 的下一个下标
        return ans
