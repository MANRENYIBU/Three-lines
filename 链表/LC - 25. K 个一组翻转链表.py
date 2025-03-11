#  题目来源：https://leetcode.cn/problems/reverse-nodes-in-k-group/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 获取链表长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        p0 = dummy = ListNode(next = head)
        pre = None
        cur = p0.next
        
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
