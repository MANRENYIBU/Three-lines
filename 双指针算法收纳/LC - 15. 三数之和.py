# 题目来源：https://leetcode.cn/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        nums.sort()
        
        # 相向双指针
        n = len(nums)
        ans = []
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:  # 不可以包含重复的三元组(去除重复i)
                continue
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-1] + nums[-2] < 0:
                continue
            j = i + 1  # left
            k = n - 1  # right
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:   # 不可以包含重复的三元组(去除重复j)
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:   # 不可以包含重复的三元组(去除重复k)
                        k -= 1
        return ans
