# 题目来源：https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        val = set(nums)
        cur = dummy = ListNode(next = head)
        while cur.next:
            if cur.next.val in val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
