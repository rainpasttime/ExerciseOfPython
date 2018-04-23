# -*- coding:utf-8 -*-
class Solution:
    def push(self, node):
        self.stack.append(node)
    def pop(self):
        result = self.stack[len(self.stack)-1]
        self.stack.pop()
        return result
    def top(self):
        return self.stack[len(self.stack)-1]
    def min(self):
        return min(self.stack)
    def __init__(self):
    	self.stack=[]