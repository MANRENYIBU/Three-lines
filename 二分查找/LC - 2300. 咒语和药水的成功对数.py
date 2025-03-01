# 题目来源：https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/description/

from typing import List
def lower_bound(nums: List[int], target: int)-> int:
    n = len(nums)
    left = -1
    right = n
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        success -= 1
        ans = []
        for i in spells:
            ans.append(n - lower_bound(potions, success // i + 1))
        return ans
