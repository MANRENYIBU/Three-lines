# 题目来源：https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-i/?envType=daily-question&envId=2025-04-02

from typing import List

# 方法一：遍历

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans


# 方法二：枚举 j

'''
枚举 j, 为了让 (nums[i] - nums[j])∗nums[k] 尽量大, 
我们需要知道 j 左侧元素的最大值（让 nums[i] - nums[j] 尽量大）, 
以及 j 右侧元素的最大值（让乘积尽量大）。

也就是计算 nums 的前缀最大值 preMax 和后缀最大值 sufMax, 这可以用递推预处理：
preMax[i]=max(preMax[i - 1],nums[i])
sufMax[i]=max(sufMax[i+1],nums[i])
代码实现时, 可以只预处理 sufMax 数组, preMax 可以在计算答案的同时算出来。
'''

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            suf_max[i] = max(suf_max[i + 1], nums[i])

        ans = pre_max = 0
        for j, x in enumerate(nums):
            ans = max(ans, (pre_max - x) * suf_max[j + 1])
            pre_max = max(pre_max, x)
        return ans


# 方法三：枚举 k

'''
枚举 k, 我们需要知道 k 左边 nums[i] - nums[j] 的最大值。

类似 121. 买卖股票的最佳时机, 为了计算 nums[i] - nums[j] 的最大值, 我们需要知道 j 左边的 nums[i] 的最大值。

因此, 在遍历的过程中：
维护 nums[i] 的最大值 preMax。
维护 preMax - nums[j] 的最大值 maxDiff。
计算 maxDiff⋅nums[k], 更新答案的最大值。
代码实现时, 要先更新 ans, 再更新 maxDiff, 最后更新 preMax。为什么?

这个顺序是精心设置的：
首先更新 ans, 此时 maxDiff 还没有更新, 表示在当前元素左边的两个数的最大差值。
然后更新 maxDiff, 此时 preMax 还没有更新, 表示在当前元素左边的最大值。
最后更新 preMax。

能否修改更新顺序？
ans 依赖 maxDiff, maxDiff 依赖 preMax。如果修改更新顺序, 那么 maxDiff 或者 preMax 会包含当前元素, 
就不是左边元素的计算结果了, 这违反了题目 i<j<k 的规定。
'''

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_diff = pre_max = 0
        for x in nums:
            ans = max(ans, max_diff * x)
            max_diff = max(max_diff, pre_max - x)
            pre_max = max(pre_max, x)
        return ans
