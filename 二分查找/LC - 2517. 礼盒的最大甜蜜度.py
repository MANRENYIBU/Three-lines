# 题目来源：https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/description/

'''
定义 f(d) 表示甜蜜度至少为 d 时, 最多能选多少类糖果; 

二分答案 d:
如果 f(d) ≥ k, 说明答案至少为 d; 
如果 f(d) < k, 说明答案至多为 d - 1; 
二分结束后, 设答案为 d0, 那么 f(d0) ≥ k 且 f(d0 + 1) < k; 

如何计算 f(d)?
对 price 从小到大排序, 贪心地计算 f(d):
第一个数 price[0] 一定可以选; 
假设上一个选的数是 pre, 那么当 price[i]≥pre+d 时, 才可以选 price[i]; 
'''

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(d: int) -> int:
            cnt = 1
            pre = price[0]  # 先选一个最小的甜蜜度
            for p in price:
                if p >= pre + d:  # 可以选
                    cnt += 1
                    pre = p  # 上一个选的甜蜜度
            return cnt

        price.sort()
        left = 0
        right = (price[-1] - price[0]) // (k - 1) + 1
        while left + 1 < right:  # 开区间不为空
            # 循环不变量：
            # f(left) >= k
            # f(right) < k
            mid = (left + right) // 2
            if f(mid) >= k:
                left = mid  # 下一轮二分 (mid, right)
            else:
                right = mid  # 下一轮二分 (left, mid)
        return left  # 最大的满足 f(left) >= k 的数
