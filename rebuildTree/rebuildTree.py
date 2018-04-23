# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
        	return None
        if len(pre)==1:            #只有一个节点
        	return TreeNode(pre[0])
        else:
        	output = TreeNode(pre[0])
        	index = tin.index(pre[0])
        	output.left = self.reConstructBinaryTree(pre[1:1+index], tin[0:index])
        	output.right = self.reConstructBinaryTree(pre[1+index:], tin[index+1:])
        return output