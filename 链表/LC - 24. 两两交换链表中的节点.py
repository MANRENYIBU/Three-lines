# 题目来源：https://leetcode.cn/problems/swap-nodes-in-pairs/

# 方法一：递归

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 递归边界
            return head  # 不足两个节点，无需交换

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)  # 1 指向递归返回的链表头
        node2.next = node1  # 2 指向 1

        return node2  # 返回交换后的链表头节点


# 方法二：迭代

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node0 = dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        node1 = head
        while node1 and node1.next:  # 至少有两个节点
            node2 = node1.next
            node3 = node2.next

            node0.next = node2  # 0 -> 2
            node2.next = node1  # 2 -> 1
            node1.next = node3  # 1 -> 3

            node0 = node1  # 下一轮交换，0 是 1
            node1 = node3  # 下一轮交换，1 是 3
        return dummy.next  # 返回新链表的头节点


# 方法三：采用k个一组的迭代的代码

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 获取链表长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        p0 = dummy = ListNode(next = head)
        pre = None
        cur = p0.next
        
        while n >= 2:  # k = 2
            n -= 2
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
