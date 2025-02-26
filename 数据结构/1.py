# 题目来源：https://leetcode.cn/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url):
        self.cur += 1
        del self.history[self.cur:]
        self.history.append(url)

    def back(self, steps):
        self.cur = max(self.cur - steps, 0)
        return self.history[self.cur]

    def forward(self, steps):
        self.cur = min(self.cur + steps, len(self.history) - 1)
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)