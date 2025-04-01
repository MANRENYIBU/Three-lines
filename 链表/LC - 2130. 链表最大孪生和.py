# 题目来源：https://leetcode.cn/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        ans = 0
        while head2:
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return ans
