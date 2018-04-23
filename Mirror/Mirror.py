# -*- coding:utf-8 -*-
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root==None:
        	return None
        if root.left!=None:
        	self.Mirror(root.left)
        if root.right!=None:
        	self.Mirror(root.right)
        temTree = root.left
        root.left = root.right
        root.right = temTree
        return root