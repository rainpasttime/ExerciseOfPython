# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def display(self):
    	print self.val
    	if self.left!=None:
    		self.left.display()
    	else:
    		print "#"
    	if self.right!=None:
    		self.right.display()
    	else:
    		print "#"