# 题目来源：https://leetcode.cn/problems/the-number-of-beautiful-subsets/description/

'''
在选择 x = nums[i] 的时候, 如果之前选过 x - k 或 x + k, 则不能选, 否则可以选; 
代码实现时, 可以用哈希表（或者数组）记录选过的数及其出现次数, 从而 O(1) 判断 x - k 和 x + k 是否选过; 
'''

# 写法一：输入视角，选或不选

from collections import defaultdict
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = defaultdict(int)

        # nums[i] 选或不选
        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)  # 不选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:  # 可以选
                cnt[x] += 1  # 选
                dfs(i + 1)  # 讨论 nums[i+1] 选或不选
                cnt[x] -= 1  # 撤销，恢复现场

        dfs(0)
        return ans


# 写法二：答案视角，枚举选哪个

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = defaultdict(int)

        # 在 [i, n-1] 中选一个数
        def dfs(i: int) -> None:
            nonlocal ans
            ans += 1
            if i == len(nums):
                return
            for j in range(i, len(nums)):  # 枚举选哪个
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:  # 可以选
                    cnt[x] += 1  # 选
                    dfs(j + 1)  # 下一个数在 [j+1, n-1] 中选
                    cnt[x] -= 1  # 撤销，恢复现场

        dfs(0)
        return ans
