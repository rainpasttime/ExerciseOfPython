# # -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         if n ==1:
#         	return 1
#         elif n==2:
#         	return 1
#         else:
#         	return self.Fibonacci(n-1)+self.Fibonacci(n-2)


# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
        	return 0
        elif n ==1:
        	return 1
        elif n==2:
        	return 1
        else:
        	a = 2
        	b = 3
        	index = 3
        	while(index!=n):
        		a = a+b
        		c = b
        		b = a
        		a = c
        		index = index +1
        return a