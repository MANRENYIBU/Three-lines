# 题目来源：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        # 暴力遍历(TLE)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers [j] == target:
                    return [i + 1, j + 1]

        # 相向双指针
        left = 0
        right = n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                break
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]
