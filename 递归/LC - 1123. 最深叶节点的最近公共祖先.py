# 题目来源：https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/description/?envType=daily-question&envId=2025-04-04

# 方法一：递归

'''
对于本题, 要找的节点是最深的叶子。
如果左子树的最大深度比右子树的大, 那么（子树中的）最深叶子就只在左子树中, 所以（子树中的）最深叶子的最近公共祖先也只在左子树中。
如果左右子树的最大深度一样呢？当前节点一定是最近公共祖先吗？
不一定。比如上图节点 1 的左右子树最深叶子 0,8 的深度都是 2, 但该深度并不是全局最大深度, 所以节点 1 并不是答案。

根据以上讨论, 正确做法如下：
从根节点开始递归, 同时维护全局最大深度 maxDepth。
在「递」的时候往下传 depth, 用来表示当前节点的深度。
在「归」的时候往上传当前子树最深的空节点的深度。这里为了方便, 用空节点代替叶子, 因为最深的空节点的上面一定是最深的叶子。
设左子树最深空节点的深度为 leftMaxDepth, 右子树最深空节点的深度为 rightMaxDepth。
如果最深的空节点左右子树都有, 即 leftMaxDepth=rightMaxDepth=maxDepth, 那么更新答案为当前节点。
注意这并不代表我们找到了答案, 如果后面发现了更深的空节点, 答案还会更新。另外注意, 这个判断方式在只有一个最深叶子的情况下, 也是正确的。
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        md = -1
        def dfs(node, d):
            nonlocal ans, md
            if node is None:
                md = max(md, d)
                return d
            left_md = dfs(node.left, d + 1)
            right_md = dfs(node.right, d + 1)
            if left_md == right_md == md:
                ans = node
            return max(left_md, right_md)
        dfs(root, 0)
        return ans


# 方法二：自底向上

'''
能否不用外部变量 ans 和 maxDepth 呢？

把每棵子树都看成是一个「子问题」, 即对于每棵子树, 我们需要知道：
这棵子树最深叶子的深度。这里是指叶子在这棵子树内的深度, 而不是在整棵二叉树的视角下的深度。相当于这棵子树的高度。
这棵子树的最深叶子的最近公共祖先 lca。

设子树的根节点为 node, node 的左子树的高度为 leftHeight, node 的右子树的高度为 rightHeight。分类讨论：
如果 leftHeight>rightHeight, 那么 node 子树的高度为 leftHeight+1, lca 是左子树的 lca。
如果 leftHeight<rightHeight, 那么 node 子树的高度为 rightHeight+1, lca 是右子树的 lca。
如果 leftHeight=rightHeight, 那么 node 子树的高度为 leftHeight+1, lca 就是 node。
'''

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return 0, None
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)
            if left_height > right_height:  # 左子树更高
                return left_height + 1, left_lca
            if left_height < right_height:  # 右子树更高
                return right_height + 1, right_lca
            return left_height + 1, node  # 一样高
        return dfs(root)[1]
