# 题目来源：https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2025-03-19

# 方法一：模拟

from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)  # 统计每个元素的出现次数
        while cnt:  # 还有剩余元素
            row = list(cnt)
            ans.append(row)
            # cnt 中的每个元素的出现次数都减一
            for x in row:
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]  # 去掉出现次数为 0 的元素
        return ans


# 方法二：一次遍历

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = [0] * (len(nums) + 1)
        for x in nums:
            if cnt[x] == len(ans):  # 需要加一行
                ans.append([])
            ans[cnt[x]].append(x)
            cnt[x] += 1
        return ans
