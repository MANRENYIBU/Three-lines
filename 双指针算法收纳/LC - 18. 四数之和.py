# 题目来源：https://leetcode.cn/problems/4sum/

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n - 3):
            x = nums[a]
            if a > 0 and x == nums[a - 1]:  # 跳过重复a
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if x + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for b in range(a + 1, n - 2):
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]:  # 跳过重复b
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:
                    break
                if x + y + nums[-1] + nums[-2] < target:
                    continue
                
                c = b + 1  # left
                d = n - 1  # right
                while c < d:
                    s = x + y + nums[c] + nums[d]
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复c
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:  # 跳过重复d
                            d -= 1
        return ans
