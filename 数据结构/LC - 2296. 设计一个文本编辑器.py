# 题目来源：https://leetcode.cn/problems/design-a-text-editor/description/

# 方法一：对顶栈
'''
创建左右两个栈，头对头（栈顶对栈顶），光标的左右移动就相当于两个栈中的数据来回倒（左手倒右手，右手倒左手）
对于插入和删除操作，直接在左边那个栈上入栈出栈
'''

class TextEditor:
    def __init__(self):
        self.left = []  # 光标左侧字符
        self.right = []  # 光标右侧字符

    def addText(self, text: str) -> None:
        self.left.extend(text)  # 入栈

    def deleteText(self, k: int) -> int:
        pre = len(self.left)  # 删除之前的栈大小
        del self.left[-k:]  # 出栈
        return pre - len(self.left)  # 减去删除之后的栈大小

    def text(self) -> str:
        return ''.join(self.left[-10:])  # 光标左边至多 10 个字符

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.append(self.left.pop())  # 左手倒右手
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())  # 右手倒左手
            k -= 1
        return self.text()


# 方法二：Splay（选读）
'''
如果 k 很大，要怎么做？有没有复杂度和 k 无关的算法？
可以用 Splay 模拟文本的添加和删除。感兴趣的同学可以查阅相关资料
'''

class Node:
    def __init__(self, key: str):
        self.ch = [None, None]  # 左子节点ch[0]，右子节点ch[1]
        self.sz = 1             # 子树大小
        self.key = key          # 节点字符

    def cmpKth(self, k: int) -> int:
        left_size = self.ch[0].sz if self.ch[0] else 0
        d = k - left_size - 1
        if d < 0:
            return 0    # 左子树
        elif d > 0:
            return 1    # 右子树
        else:
            return -1   # 当前节点

    def maintain(self) -> None:
        self.sz = 1
        if self.ch[0]:
            self.sz += self.ch[0].sz
        if self.ch[1]:
            self.sz += self.ch[1].sz

    def rotate(self, d: int) -> 'Node':
        x = self.ch[d ^ 1]
        self.ch[d ^ 1] = x.ch[d]
        x.ch[d] = self
        self.maintain()
        x.maintain()
        return x

    def splay(self, k: int) -> 'Node':
        d = self.cmpKth(k)
        if d < 0:
            return self
        left_size = self.ch[0].sz if self.ch[0] else 0
        k -= d * (left_size + 1)
        c = self.ch[d]
        if c is None:
            return self.rotate(d ^ 1)
        d2 = c.cmpKth(k)
        if d2 >= 0:
            c_left_size = c.ch[0].sz if c.ch[0] else 0
            new_k = k - d2 * (c_left_size + 1)
            c.ch[d2] = c.ch[d2].splay(new_k)
            if d2 == d:
                self.ch[d] = c
                new_self = self.rotate(d ^ 1)
            else:
                self.ch[d] = c.rotate(d)
                new_self = self
            return new_self.rotate(d ^ 1)
        else:
            return self.rotate(d ^ 1)

    def split(self, k: int):
        lo = self.splay(k)
        ro = lo.ch[1]
        lo.ch[1] = None
        lo.maintain()
        return lo, ro

    def merge(self, ro: 'Node') -> 'Node':
        if self is None:
            return ro
        self = self.splay(self.sz)
        self.ch[1] = ro
        self.maintain()
        return self

def buildSplay(s: str) -> Node:
    if not s:
        return None
    m = len(s) // 2
    o = Node(s[m])
    o.ch[0] = buildSplay(s[:m])
    o.ch[1] = buildSplay(s[m+1:])
    o.maintain()
    return o

class TextEditor:
    def __init__(self):
        self.root = None
        self.cur = 0

    def addText(self, text: str) -> None:
        if not text:
            return
        new_tree = buildSplay(text)
        if self.cur == 0:
            self.root = new_tree.merge(self.root) if self.root else new_tree
        else:
            lo, ro = self.root.split(self.cur)
            merged_lo = lo.merge(new_tree)
            self.root = merged_lo.merge(ro) if ro else merged_lo
        self.cur += len(text)

    def deleteText(self, k: int) -> int:
        if self.cur == 0 or not self.root:
            return 0
        actual_k = min(k, self.cur)
        if self.cur <= actual_k:
            _, self.root = self.root.split(self.cur)
            deleted = self.cur
            self.cur = 0
            return deleted
        else:
            lo, ro = self.root.split(self.cur)
            new_lo, _ = lo.split(self.cur - actual_k)
            self.root = new_lo.merge(ro) if ro else new_lo
            self.cur -= actual_k
            return actual_k

    def cursorLeft(self, k: int) -> str:
        self.cur = max(self.cur - k, 0)
        return self._text()

    def cursorRight(self, k: int) -> str:
        max_cur = self.root.sz if self.root else 0
        self.cur = min(self.cur + k, max_cur)
        return self._text()

    def _text(self) -> str:
        if self.cur == 0 or not self.root:
            return ""
        k = max(self.cur - 10, 0)
        required = self.cur - k
        if required <= 0:
            return ""
        self.root = self.root.splay(k + 1)
        ans = [self.root.key]
        remain = required - 1
        if remain <= 0:
            return ''.join(ans)
        def inorder(node):
            nonlocal ans, remain
            if not node or remain <= 0:
                return
            inorder(node.ch[0])
            if remain <= 0:
                return
            ans.append(node.key)
            remain -= 1
            inorder(node.ch[1])
        inorder(self.root.ch[1])
        return ''.join(ans[:required])
