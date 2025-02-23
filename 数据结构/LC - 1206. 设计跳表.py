# 题目来源：https://leetcode.cn/problems/design-skiplist/description/

'''
跳表的详细介绍: https://www.jianshu.com/p/9d8296562806

先创建一个跳表节点Node, 需要包含以下三个参数: 
节点值val
右边节点right
下边节点down

跳表初始化
每一层设置左右两个哨兵节点, 左节点的值要比所有值小, 右节点的值要比所有值大。因为0 <= num, target <= 20000, 因此左节点值设为 -1, 右节点值设为20001即可
跳表的最大层数为16。因为题目说了最多调用 50000 次 search, add, 以及 erase操作, 也就是底层链表长度n最长为50000
而我们随机的选n/2个元素做为一级索引, 随机选n/4个元素作为二级索引, 随机选n / (2**k)作为顶层索引。而2 **16 = 65536 > 50000, 所以16层足够为长度50000的链表建立索引
每层的两个哨兵节点中, 左节点要指向右节点, 并且除了最后一层外左右节点都需要指向下一层节点跳表起始节点head即为left[0], 即顶层的左哨兵节点

查找(search)方法
从head节点开始查找, 如果当前节点cur的右边节点值比target大, 应该往下查找: 如果cur的右边节点值比target小, 应该往右查找: 如果相等, 那就是找到了, 返回True。遍历完了也没找到, 返回False

插入(add)方法
相对比较复杂, 因为还需要根据概率维护索引, 查找插入位置。也是从head开始查找插入的位置, 每次往下走的节点都需要保存, 因为可能在该节点后面插入新的节点作为索引
换句话说, 其实查找的是在每一层应该插入的位置并记录在stack中, 只是不一定每一层都会插入节点罢了
插入节点。首先最后一层肯定是要插入节点的, 插入完成后, 记录一下该层节点, 因为如果该节点要加入到索引中, 上一层是要指向这一层的
以1/2的概率生成索引, 在上一层插入节点: 1/2的概率插入结束, 不再继续维护索引: 如果前面生成了索引, 再以1/2的概率插入节点直到插入到顶层或中途因概率停止插入

删除(erase)方法
删除和查找差不多, 只不过是对每一层找到的节点都要进行删除, 也就是删除节点的同时要删除由其产生的索引节点

实现代码如下：
'''

import random

class Node:
    def __init__(self, val):
        self.val = val
        self.down = None
        self.right = None

class Skiplist:

    def __init__(self):
        left = []
        for _ in range(16):
            left.append(Node(-1))
        right = []
        for _ in range(16):
            right.append(Node(20001))
        
        for i in range(15):
            left[i].right = right[i]
            left[i].down = left[i + 1]
            right[i].down = right[i + 1]
        left[-1].right = right[-1]
        self.head = left[0]
        
    def search(self, target):
        cur = self.head
        while cur:
            if cur.right.val > target:
                cur = cur.down
            elif cur.right.val < target:
                cur = cur.right
            else:
                return True
        return False

    def add(self, num):
        cur = self.head
        stack = []
        while cur:
            if cur.right.val >= num:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.right
        pre = None

        while stack:
            cur = stack.pop()
            node = Node(num)
            node.right = cur.right
            cur.right = node
            if pre:
                node.down = pre
            pre = node
            if random.randint(0, 1):
                break

    def erase(self, num):
        cur = self.head
        is_removed = False
        while cur:
            if cur.right.val >= num:
                if cur.right.val == num:
                    is_removed = True
                    cur.right = cur.right.right
                cur = cur.down
            else:
                cur = cur.right
        return is_removed



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)