# -*- coding:utf-8 -*-
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root==None:
        	return []
        result = []
        now = []
        self.FindPathReverse(root,expectNumber,0,result,now)
        return result

    def FindPathReverse(self,root,expectNumber,length,result,now):
    	new_length = length + root.val
    	if new_length>expectNumber:
    			return 
    	elif root.left==None and root.right==None and new_length==expectNumber:
    		now.append(root.val)
    		tem = now[:]
    		result.append(tem)
    		del now[-1]
    		return
    	elif root.left==None and root.right==None and new_length!=expectNumber:
    		return
    	now.append(root.val)
    	if root.left!=None:
    		self.FindPathReverse(root.left,expectNumber,new_length,result,now)
    	if root.right!=None:
    		self.FindPathReverse(root.right,expectNumber,new_length,result,now)
    	del now[-1]
    	return