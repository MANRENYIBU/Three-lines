        '''
        # https://leetcode.cn/problems/cat-and-mouse/
        dfs(step, i, j):
        step: 已经进行的游戏步数
        i: 老鼠位置
        j: 猫位置
        边界: i = 0 return 1
        j = i return 2
        那平局应该怎么表示呢？
        根据题目，平局可以理解为猫和老鼠在某个环内绕圈（也就是博弈的平衡点）：
        在 n 个节点中，老鼠可以有 n 种可能而猫只能有 (n - 1) 种可能，
        总共是两个玩家轮流行动，也即每个 (i, j) 位置都有两种可能的行动者；
        因此，游戏的所有可能局面是 2 * n * (n - 1)，
        所以可以用 已经进行的游戏步数 大于等于 总轮数 来表示平局，
        这可以被理解为有限状态自动机的所有状态都被访问过，从而进入循环（某个环内绕圈）。
        因此，step ≥ 2 * n * (n - 1) return 0
        参考代码如下（会TEL）：
        '''

class Solution:
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
根据题目描述，游戏中的状态由老鼠的位置、猫的位置和移动方决定。当状态为以下情况，可以直接确定胜负：

当猫和老鼠的位置相同时，猫获胜，这是猫的必胜状态，老鼠的必败状态。
当老鼠位于洞时，老鼠获胜，这是老鼠的必胜状态，猫的必败状态。
为了得到初始状态的游戏结果，需要从边界状态开始遍历所有的状态。每个状态包含老鼠的位置、猫的位置和移动方，根据当前状态可以得到上一轮的所有可能状态，上一轮状态的移动方和当前状态的移动方相反，上一轮状态的移动方在上一轮状态的位置和当前状态的位置不同。

我们用元组 (m,c,t) 表示本轮的状态，用 (pm,pc,pt) 表示上一轮可能的状态，那么上一轮的所有可能状态有：

如果本轮的移动方是老鼠，那么上一轮的移动方是猫，上一轮的老鼠位置是本轮老鼠位置，上一轮的猫位置是本轮猫位置的所有邻接点。
如果本轮的移动方是猫，那么上一轮的移动方是老鼠，上一轮的猫位置是本轮猫位置，上一轮的老鼠位置是本轮老鼠位置的所有邻接点。
初始时，除了边界状态以外，其他所有状态的结果都是未知的。我们从边界状态开始，对于每个状态，得到上一轮的所有可能状态并更新结果，更新的逻辑如下：

如果上一轮的移动方与本轮的获胜方相同，那么上一轮的移动方可以到达当前状态并获胜，直接更新上一轮的状态为本轮的获胜方。
如果上一轮的移动方与本轮的获胜方不同，且上一轮的移动方可以到达的所有状态都是上一轮的移动方的必败状态，那么我们将上一轮的状态更新为本轮的获胜方。
对于第 2 个更新逻辑，我们需要记录每个状态的度。初始时，每个状态的度表示该状态的移动方可以移动到的结点数，即移动方所在节点的相邻结点数，如果移动方是猫且所在结点与洞相邻则需要将该状态的度减 1。

当所有状态的结果都更新完毕时，初始状态的结果即为最终结果。
'''

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        degree = [[[0]*2 for _ in range(n)] for _ in range(n)]
        res = [[[0]*2 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degree[i][j][0] = len(graph[i])
                degree[i][j][1] = len(graph[j])
        for i in graph[0]:
            for j in range(n):
                degree[j][i][1] -= 1
        cand = []
        for i in range(1, n):
            res[0][i][0] = res[0][i][1] = 1
            cand.append((0, i, 0))
            cand.append((0, i, 1))
            res[i][i][0] = res[i][i][1] = 2
            cand.append((i, i, 0))
            cand.append((i, i, 1))
        while cand:
            tmp = []
            for m, c, t in cand:
                cur = res[m][c][t]
                if t == 0:
                    for x in graph[c]:
                        if x == 0:
                            continue
                        if res[m][x][1] == 0:
                            if cur == 2:
                                res[m][x][1] = 2
                                tmp.append((m, x, 1))
                            else:
                                degree[m][x][1] -= 1
                                if degree[m][x][1] == 0:
                                    res[m][x][1] = 1
                                    tmp.append((m, x, 1))
                else:
                    for x in graph[m]:
                        if res[x][c][0] == 0:
                            if cur == 1:
                                res[x][c][0] = 1
                                tmp.append((x, c, 0))
                            else:
                                degree[x][c][0] -= 1
                                if degree[x][c][0] == 0:
                                    res[x][c][0] = 2
                                    tmp.append((x, c, 0))
            cand = tmp
        return res[1][2][0]
