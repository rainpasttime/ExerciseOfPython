# -*- coding:utf-8 -*-
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        queen = []
        index = -1
        if root == None:
        	return result
        else:
        	queen.append(root)
        	while index!=len(queen)-1:
        		index = index+1
        		tem_node = queen[index]
        		result.append(tem_node.val)
        		if tem_node.left!=None:
        			queen.append(tem_node.left)
        		if tem_node.right!=None:
        			queen.append(tem_node.right)
        	return result