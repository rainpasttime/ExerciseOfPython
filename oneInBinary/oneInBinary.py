# # -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        a = []
        print type(n)
        for i in range(0,32):     #int 类型有32位
        	a.append(n>>i & 1)
        return sum(a)