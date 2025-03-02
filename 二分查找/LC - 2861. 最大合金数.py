# 题目来源：https://leetcode.cn/problems/maximum-number-of-alloys/

'''
挨个判断每台机器最多可以制造多少份合金。
假设要制造 num 份合金, 由于 num 越小, 花费的钱越少, num 越多, 花费的钱越多, 有单调性, 可以二分。

对于第 j 类金属：

如果 composition[i][j] * num≤stock[j], 那么无需购买额外的金属。
如果 composition[i][j] * num>stock[j], 那么需要购买额外的金属, 花费为
(composition[i][j] * num - stock[j]) * cost[j]
遍历每类金属, 计算总花费。如果总花费超过 budget, 则无法制造 num 份合金, 否则可以制造。

最后讨论下二分的上下界：

二分上界：粗略计算一下, 假设 composition[i][j] 和 cost[j] 都是 1, 此时可以制造最多的合金, 个数为 min(stock)+budget。
二分下界：可以设为 1。更巧妙的做法是, 设当前答案为 ans, 那么可以初始化二分下界为 ans + 1; 
因为算出小于等于 ans 的值是没有意义的, 不会让 ans 变大。如果这台机器无法制造出至少 ans + 1 份合金, 那么二分循环结束后的结果为 ans, 不影响答案。
下面的代码采用开区间写法, 要把上界加一, 下界减一。
'''

from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        mx = min(stock) + budget
        for comp in composition:
            def check(num: int) -> bool:
                money = 0
                for s, base, c in zip(stock, comp, cost):
                    if s < base * num:
                        money += (base * num - s) * c
                        if money > budget:
                            return False
                return True

            left, right = ans, mx + 1
            while left + 1 < right:  # 开区间写法
                mid = (left + right) // 2
                if check(mid):
                    left = mid
                else:
                    right = mid
            ans = left
        return ans
