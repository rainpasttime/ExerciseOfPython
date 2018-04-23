# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []
    def push(self,node):
        # write code here
        self.stack_one.append(node)
    def pop(self):
        self.stack_two = []
        length = len(self.stack_one)
        for i in range(length):
            self.stack_two.append(self.stack_one[length-i-1])
        self.stack_one = []
        for i in range(length-1):
            self.stack_one.append(self.stack_two[length-i-2])
        return self.stack_two[length-1]
        # return xx