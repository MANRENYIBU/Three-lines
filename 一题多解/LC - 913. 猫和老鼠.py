# 题目来源：https://leetcode.cn/problems/cat-and-mouse/

'''
        dfs(step, i, j):
        step: 已经进行的游戏步数
        i: 老鼠位置
        j: 猫位置
        边界: i = 0 return 1
        j = i return 2
        那平局应该怎么表示呢？
        根据题目, 平局可以理解为猫和老鼠在某个环内绕圈(也就是博弈的平衡点)：
        在 n 个节点中, 老鼠可以有 n 种可能而猫只能有 (n - 1) 种可能, 
        总共是两个玩家轮流行动, 也即每个 (i, j) 位置都有两种可能的行动者；
        因此, 游戏的所有可能局面是 2 * n * (n - 1), 
        所以可以用 已经进行的游戏步数 大于等于 总轮数 来表示平局, 
        这可以被理解为有限状态自动机的所有状态都被访问过, 从而进入循环(某个环内绕圈)。
        因此, step ≥ 2 * n * (n - 1) return 0
'''

# 参考代码如下(会TEL)：
from typing import List
from functools import cache

def catMouseGame(self, graph: List[List[int]]) -> int:
    n = len(graph)

    @cache
    def dfs(step, i, j):
        if i == 0:
            return 1
        if j == i:
            return 2
        if step >= 2 * n * (n - 1):
            return 0

        if step % 2 == 0:  # 老鼠行动
            win, draw = False, False
            for next_s in graph[i]:
                res = dfs(step + 1, next_s, j)
                if res == 1:
                    win = True
                    break
                elif res == 0:
                    draw = True
            if win:
                return 1
            else:
                if draw:
                    return 0
                else:
                    return 2
        else:  # 猫行动
            win, draw = False, False
            for next_s in graph[j]:
                if next_s == 0:
                    continue  # 猫不能进入洞口
                res = dfs(step + 1, i, next_s)
                if res == 2:
                    win = True
                    break
                elif res == 0:
                    draw = True
            if win:
                return 2
            else:
                if draw:
                    return 0
                else:
                    return 1
    return dfs(0, 1, 2)  # 状态入口


# 参考解法：拓扑排序

'''
初步分析
我们要解决的原问题是：

鼠在节点 1, 猫在节点 2, 当前轮到鼠移动, 最终谁获胜(或者平局)。
假如鼠从节点 1 移动到相邻节点 3, 那么问题变成：

鼠在节点 3, 猫在节点 2, 当前轮到猫移动, 最终谁获胜(或者平局)。
这是和原问题相似的问题, 可以用递归解决。

但这是「规模更小的子问题」吗？不是。因为猫鼠可以左右横跳、重复移动(递归结构有环), 可能会无限递归下去, 也就是平局。

这说明从起点出发, 是不好解决的。

逆向思维
正难则反, 从终点开始倒推, 能否得到一个鼠在节点 1, 猫在节点 2, 当前轮到鼠移动的状态？

终点是什么？

如果鼠移动到洞中(节点 0), 那么鼠获胜。
如果猫鼠相遇, 那么猫获胜。
从终点倒推一步：

比如 0 和 3 相连, 如果上一步鼠在节点 3, 猫在节点 4, 轮到鼠移动, 那么鼠可以移动到洞中, 
所以这种(鼠在节点 3, 猫在节点 4, 轮到鼠移动)的状态, 就可以直接标记为「鼠获胜」。
比如 6 和 7 相连, 如果上一步鼠在节点 6, 猫在节点 7, 轮到猫移动, 那么猫可以移动到 6 和鼠相遇, 
所以这种(鼠在节点 6, 猫在节点 7, 轮到猫移动)的状态, 就可以直接标记为「猫获胜」。
除此以外, 还有两种情况, 也可以确定谁一定是获胜的。举例说明：

如果发现从(鼠在节点 8, 猫在节点 9, 轮到鼠移动)这种状态继续游戏, 能到达的状态都是「猫获胜」, 
那么这种(鼠在节点 8, 猫在节点 9, 轮到鼠移动)的状态可以标记为「猫获胜」。
如果发现从(鼠在节点 8, 猫在节点 9, 轮到猫移动)这种状态继续游戏, 能到达的状态都是「鼠获胜」, 
那么这种(鼠在节点 8, 猫在节点 9, 轮到猫移动)的状态可以标记为「鼠获胜」。
状态表示
定义：

winner[i][j][0] 表示鼠在节点 i, 猫在节点 j, 轮到鼠移动, 最终谁获胜。
winner[i][j][1] 表示鼠在节点 i, 猫在节点 j, 轮到猫移动, 最终谁获胜。
winner[i][j][k]=0 表示「尚未确定」或者「平局」。
winner[i][j][k]=1 表示「鼠获胜」。
winner[i][j][k]=2 表示「猫获胜」。
终点：

如果鼠移动到洞中(节点 0), 那么鼠获胜。注意这里可以只考虑鼠在洞中, 且轮到猫移动的状态, 无需考虑继续轮到鼠移动的状态。即 winner[0][j][1]=1。
如果猫鼠相遇, 那么猫获胜。即 winner[i][i][0]=winner[i][i][1]=2。
倒推：

情况一：如果 winner[i][j][1]=1, 倒推上一个状态(鼠在节点 i`, 猫在节点 j, 轮到鼠移动), 那么鼠从 i`移动到 i 即可确保获胜, 所以有 winner[i`][j][0]=1。
情况二：如果 winner[i][j][0]=2, 倒推上一个状态(鼠在节点 i, 猫在节点 j`, 轮到猫移动), 那么猫从 j`移动到 j 即可确保获胜, 所以有 winner[i][j`][1]=2。
情况三：倒推上一个状态(鼠在节点 i`, 猫在节点 j, 轮到鼠移动), 且无论鼠怎么移动, 都是猫赢(甚至不能平局), 那么标记 winner[i`][j][0]=2。
情况四：倒推上一个状态(鼠在节点 i, 猫在节点 j`, 轮到猫移动), 且无论猫怎么移动, 都是鼠赢(甚至不能平局), 那么标记 winner[i][j`][1]=1。

起点(答案)：
鼠在节点 1, 猫在节点 2, 当前轮到鼠移动, 即 winner[1][2][0]。
注：如果最终 winner[1][2][0]=0, 说明无法从终点倒推得到, 也就是无法从起点移动到终点(鼠获胜或者猫获胜), 即平局。

编程细节:
设当前状态为 winner[i][j][k], 那么上一个状态的 k`=k⊕1(k 异或 1)。这样可以在 0 和 1 之间切换。
情况一和情况二可以合并为：如果发现 k`=winner[i][j][k] - 1, 那么上一个状态的值就是 winner[i][j][k]。

下面代码把 graph 简记为 g。
'''

from collections import deque
from typing import List, Tuple

class Solution:
    def catMouseGame(self, g: List[List[int]]) -> int:
        HOLE = 0
        n = len(g)
        deg = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                deg[i][j][0] = len(g[i])
                deg[i][j][1] = len(g[j])
            # 对于猫来说，所有连到洞的边都不能走
            for j in g[HOLE]:
                deg[i][j][1] -= 1

        winner = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()
        for i in range(1, n):
            winner[HOLE][i][1] = 1  # 鼠到达洞中（此时轮到猫移动），鼠获胜
            winner[i][i][0] = winner[i][i][1] = 2  # 猫和鼠出现在同一个节点，无论轮到谁移动，都是猫获胜
            q.append((HOLE, i, 1))  # 从终点开始倒推
            q.append((i, i, 0))
            q.append((i, i, 1))

        # 获取 (mouse, cat, turn) 的上个状态（值尚未确定）
        def get_pre_states() -> List[Tuple[int, int]]:
            if turn:  # 当前轮到猫移动，枚举上一轮鼠的位置
                return [(pre_mouse, cat) for pre_mouse in g[mouse] if winner[pre_mouse][cat][0] == 0]
            # 当前轮到鼠移动，枚举上一轮猫的位置，注意猫无法移动到洞中
            return [(mouse, pre_cat) for pre_cat in g[cat] if pre_cat != HOLE and winner[mouse][pre_cat][1] == 0]

        # 减少上个状态的度数
        def dec_deg_to_zero() -> bool:
            deg[pre_mouse][pre_cat][pre_turn] -= 1
            return deg[pre_mouse][pre_cat][pre_turn] == 0

        while q:
            mouse, cat, turn = q.popleft()
            win = winner[mouse][cat][turn]  # 最终谁赢了
            pre_turn = turn ^ 1
            for pre_mouse, pre_cat in get_pre_states():
                # 情况一：如果上一回合鼠从 pre 移动到 cur，最终鼠赢，那么标记 pre 状态的 winner = 鼠
                # 情况二：如果上一回合猫从 pre 移动到 cur，最终猫赢，那么标记 pre 状态的 winner = 猫
                # 情况三：如果上一回合鼠从 pre 移动到 cur，最终猫赢，那么待定，直到我们发现从 pre 出发能到达的状态都是猫赢，那么标记 pre 状态的 winner = 猫
                # 情况四：如果上一回合猫从 pre 移动到 cur，最终鼠赢，那么待定，直到我们发现从 pre 出发能到达的状态都是鼠赢，那么标记 pre 状态的 winner = 鼠
                if pre_turn == win - 1 or dec_deg_to_zero():
                    winner[pre_mouse][pre_cat][pre_turn] = win
                    q.append((pre_mouse, pre_cat, pre_turn))  # 继续倒推

        # 鼠在节点 1，猫在节点 2，当前轮到鼠移动
        return winner[1][2][0]  # 返回最终谁赢了（或者平局）
