# 题目来源：https://leetcode.cn/problems/design-an-ordered-stream/description/

class OrderedStream:

    def __init__(self, n):
        self.data = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        self.data[idKey - 1] = value
        ans = []
        while self.ptr < len(self.data) and self.data[self.ptr]:  # 返回值要按照当时的ptr来判断
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
