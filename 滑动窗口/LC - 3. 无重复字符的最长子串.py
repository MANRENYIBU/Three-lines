# 题目来源：https://leetcode.cn/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s):
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
