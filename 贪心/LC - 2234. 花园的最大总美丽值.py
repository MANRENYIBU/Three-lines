# 题目来源：https://leetcode.cn/problems/maximum-total-beauty-of-the-gardens/description/?envType=daily-question&envId=2025-03-08

'''
核心思路：枚举把多少个花园种满（至少有 target 朵花）, 剩余的花种其他花园, 让最小花朵数最大; 

贪心地想, 那些要种满的花园, 原有的花朵数越多越好, 这样我们能有更多的花, 去增大花的最少数目; 
将 flowers 从小到大排序, 这样 flowers 的后缀就是要种满的花园; 
枚举 i, 把 flowers[i] 到 flowers[n - 1] 都种满花; 那么剩下要解决的问题就是, 怎么最大化花的最少数目; 

例如 flowers=[1,3,5,7,10,10], 还剩下 9 朵花:

为了增大最小值, 我们先把 flowers[0] = 1 增大, 种下 2 朵花, 增大到 flowers[1] = 3, 还剩下 9 - 2=7 朵花; 你可以把这个过程想象成我们在往前缀中倒水; 
继续种花（倒水）, 必须把 flowers[0] 和 flowers[1] 同时增大, 那么各自种下 2 朵花, 增大到 flowers[2] = 5, 还剩下 7 - 4 = 3 朵花; 
继续种花（倒水）, 必须把 flowers[0], flowers[1] 和 flowers[2] 同时增大;
由于剩余的花朵数无法让这三个花园都有 flowers[3] = 7 朵花, 所以只能平均每个花园都种 1 朵花; 
最终, flowers=[6,6,6,7,10,10], 最小的花园有 6 朵花; 换句话说, 我们把 flowers 的一个长为 3 的前缀都变成了 6 朵花; 
如果每次枚举 i, 都模拟一遍上述流程的话, 时间复杂度是 O(n ** 2), 太慢了; 

注意到, 随着 i 的变大（后缀变短）, 剩余能填充到前缀中的花也越多, 那么前缀也就越长; 
有单调性, 我们可以用双指针, 枚举 i（后缀长度）, 同时维护前缀的最长长度; 
设在填充后缀之后, 还剩下 leftFlowers 朵花可以分配; 我们把这些花种到长为 j 的前缀 [0,j−1] 中; 
设最终最小值为 avg, 那么这 j 个花园一共有 avg⋅j 朵花, 这个总数不能超过 leftFlowers 加上原有的花, 即 avg * j ≤ leftFlowers + sum[0, j - 1];
'''

from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        for i in range(n):
            flowers[i] = min(flowers[i], target)

        # 如果全部种满，还剩下多少朵花？
        left_flowers = newFlowers - (target * n - sum(flowers))

        # 没有种花，所有花园都已种满
        if left_flowers == newFlowers:
            return n * full  # 答案只能是 n*full（注意不能减少花的数量）

        # 可以全部种满
        if left_flowers >= 0:
            # 两种策略取最大值：留一个花园种 target-1 朵花，其余种满；或者，全部种满
            return max((target - 1) * partial + (n - 1) * full, n * full)

        flowers.sort()  # 时间复杂度的瓶颈在这，尽量写在后面

        ans = pre_sum = j = 0
        # 枚举 i，表示后缀 [i, n-1] 种满（i=0 的情况上面已讨论）
        for i in range(1, n + 1):
            # 撤销，flowers[i-1] 不变成 target
            left_flowers += target - flowers[i - 1]
            if left_flowers < 0:  # 花不能为负数，需要继续撤销
                continue

            # 满足以下条件说明 [0, j] 都可以种 flowers[j] 朵花
            while j < i and flowers[j] * j <= pre_sum + left_flowers:
                pre_sum += flowers[j]
                j += 1

            # 计算总美丽值
            # 在前缀 [0, j-1] 中均匀种花，这样最小值最大
            avg = (left_flowers + pre_sum) // j  # 由于上面特判了，这里 avg 一定小于 target
            total_beauty = avg * partial + (n - i) * full
            ans = max(ans, total_beauty)

        return ans
