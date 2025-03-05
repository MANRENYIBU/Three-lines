# 题目来源：https://leetcode.cn/problems/break-a-palindrome/solutions/3082264/tan-xin-pythonjavaccgojsrust-by-endlessc-plbg/

'''
palindrome 是回文串, 要改成不是回文串, 可以改任意一个不在正中心的字母, 破坏回文串的对称性, 让 palindrome 不是回文串; 
要使字典序最小, 改前面比改后面更好; 

比如 palindrome=abcba的情况: 
把左边的 b 改成 a 得到 aacba; 
把右边的 b 改成 a 得到 abcaa; 
可以发现, 前面的字母没有变小, 无论后面怎么改, 都不是最优的; 

特殊情况: 
如果 palindrome 的长度是 1, 那么无论怎么改都是回文串, 返回空串; 
如果 palindrome 除了回文中心都是字母 a, 那么只能把最后一个字母改成 b, 这样 palindrome 不是回文串, 且字典序最小; 
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'
