# 题目来源：https://leetcode.cn/problems/most-beautiful-item-for-each-query/description/?envType=daily-question&envId=2025-03-09

'''
离线算法：把 queries 排序, 通过改变回答询问的顺序, 使问题更容易处理。
在线算法：按照 queries 的顺序一个一个地回答询问。
'''

# 方法一：离线算法 + 双指针

'''
暴力的做法是, 对于每个询问 q = queries[i], 遍历 items, 计算其中 price≤q 的最大 beauty。

如何优化？

假如 queries 已经按照从小到大的顺序排好了, 例如示例 1 queries = [1,2,3,4,5,6]。

首先找所有 price≤queries[0] = 1 的物品, 求得其中最大 beauty 为 2。
然后找所有 price≤queries[1] = 2 的物品, 由于我们已经知道 price≤1 的物品的最大 beauty 为 2。
所以只需要求出 price 大于 1 且小于等于 2 的物品中的最大 beauty, 即 4, 然后计算 max(4,2) = 4, 即为所有 price≤2 的物品中的最大 beauty。
继续, 找所有 price≤queries[2]=3 的物品, 由于我们已经知道 price≤2 的物品的最大 beauty 为 4。
所以只需要求出 price 大于 2 且小于等于 3 的物品中的最大 beauty, 即 5, 然后计算 max(5,4) = 5, 即为所有 price≤3 的物品中的最大 beauty。
依此类推, 我们只需要「增量」地计算所有满足 queries[i - 1] < price≤queries[i] 的物品中的最大 beauty, 然后和上一次计算出的最大 beauty 取最大值, 即为所有 price≤queries[i] 的物品中的最大 beauty。

为此, 需要做两件事情：
把询问从小到大排序。但由于 answer 需要按照输入的顺序回答, 可以额外创建一个下标数组, 对下标数组排序。
把物品按价格从小到大排序, 这样就可以用双指针「增量」地遍历满足 queries[i - 1] < price≤queries[i] 的物品。
'''

from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: item[0])
        idx = sorted(range(len(queries)), key=lambda i: queries[i])

        ans = [0] * len(queries)
        max_beauty = j = 0
        for i in idx:
            q = queries[i]
            # 增量地遍历满足 queries[i-1] < price <= queries[i] 的物品
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            ans[i] = max_beauty
        return ans


# 方法二：在线算法 + 二分查找
# 写法一：前缀最大值

'''
示例 1 的 items=[[1,2],[3,2],[2,4],[5,6],[3,5]], 
将其按照 price 从小到大排序, 得[[1,2],[2,4],[3,2],[3,5],[5,6]]
然后原地计算其 beauty 的前缀最大值, 得[[1,2],[2,4],[3,4],[3,5],[5,6]]
注意其中 [3,2] 变成了 [3,4], 这里的 4 就是前三个物品的最大 beauty, 即 max(2,4,2) = 4。
算好前缀最大值后, 所有 price≤q 的物品的最大 beauty, 就保存在满足 price <= q 的最右边的那个物品中!
'''

from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: item[0])
        for i in range(1, len(items)):
            # 原地计算 beauty 的前缀最大值
            items[i][1] = max(items[i][1], items[i - 1][1])

        for i, q in enumerate(queries):
            j = bisect_right(items, q, key=lambda item: item[0])
            queries[i] = items[j - 1][1] if j else 0
        return queries


# 写法二：去除无用信息

'''
再来看这个排序后的 items：
[[1,2],[2,4],[3,2],[3,5],[5,6]]
其中 [3,2] 价格比 [2,4] 高, 美丽值又比 [2,4] 低, 
那么 [3,2] 就完全不如 [2,4], 可以直接去掉。（这类似单调栈/单调队列的思想）

去掉这种无用数据后, 数组变成[[1,2],[2,4],[3,5],[5,6]]
此时 beauty 就是严格递增的。
这样做的好处是 items 更短, 计算二分的时间也更短。
'''

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: item[0])
        k = 0
        for i in range(1, len(items)):
            if items[i][1] > items[k][1]:  # 有用
                k += 1
                items[k] = items[i]

        for i, q in enumerate(queries):
            j = bisect_right(items, q, 0, k + 1, key=lambda item: item[0])
            queries[i] = items[j - 1][1] if j else 0
        return queries
