# 题目来源：https://leetcode.cn/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        cnt = 0
        n = len(nums)
        for k in range(2, n):
            c = nums[k]
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > c:
                    cnt += j - i
                    j -= 1
                else:
                    i += 1
        return cnt


'''
优化: 首先把循环改成倒序枚举k
第一个优化: 在执行双指针之前, 如果发现最小的a和b相加大于c, 也就是nums[0] + nums[1] > nums[k]
说明从nums[0]到nums[k]中任选三个数a,b,c都满足a + b > c, 那么直接把 k * (k + 1) * (k - 1) // 6 (排列组合)加入答案, 退出外层循环
这是为什么要倒序枚举k的原因(正序枚举没法退出外层循环)

第二个优化: 在执行双指针之前, 如果发现最大的a和b相加小于等于c, 也就是nums[k - 2] + nums[k - 1] <= nums[k]
说明不存在 a + b > c, 不执行双指针, 继续外层循环
优化代码如下:
'''

class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        cnt = 0
        for k in range(len(nums) - 1, 1, -1):
            c = nums[k]
            if nums[0] + nums[1] > c:  # 优化一
                cnt += (k + 1) * k * (k - 1) // 6
                break
            if nums[k - 2] + nums[k - 1] <= c:  # 优化二
                continue
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > c:
                    cnt += j - i
                    j -= 1
                else:
                    i += 1
        return cnt
