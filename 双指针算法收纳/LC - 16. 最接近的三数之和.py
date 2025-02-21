# 题目来源：https://leetcode.cn/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        diff = float('inf')

        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:
                if  s - target < diff:
                    ans = s
                break
            
            s = x + nums[-1] + nums[-2]
            if s < target:
                if target - s < diff:
                    diff = target - s
                    ans = s
                continue
            
            j = i + 1  # left
            k = n - 1  # right
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < diff:
                        diff = s - target
                        ans = s
                    k -= 1
                else:
                    if target - s < diff:
                        diff = target - s
                        ans = s
                    j += 1
        return ans
