# 题目来源：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = dummy = ListNode(next = head)
        for _ in range(n):
            if not r.next:
                return head
            r = r.next
        while r.next:
            if not r.next:
                break
            if not l.next:
                break
            l = l.next
            r = r.next
        if l.next:
            l.next = l.next.next
        return dummy.next
