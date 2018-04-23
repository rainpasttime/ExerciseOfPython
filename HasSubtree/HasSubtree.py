# -*- coding:utf-8 -*-
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1==None or pRoot2==None:                        #pRoot1和pRoot2任意一个为空，就返回False
        	print "1"
        	return False
        else:
        	if pRoot1.val == pRoot2.val:       
        		flag = self.JudgeSubTree(pRoot1, pRoot2)              #判断子树
        		if flag:
        			print "2"
        			return True
        	left_flag = self.HasSubtree(pRoot1.left, pRoot2)          #判断是不是pRoot1左子树的子结构
        	if left_flag:
        		print "3"
        		return True
        	else:
        		right_flag = self.HasSubtree(pRoot1.right, pRoot2)     #判断是不是pRoot1右子树的子结构
        		print "4"
        		return right_flag

    #找到相同的根节点，比较他们的子树
    def JudgeSubTree(self,pRoot1, pRoot2):
    	if pRoot2.left!=None and pRoot1.left!=None:
    		if pRoot2.left.val==pRoot1.left.val:
    			left = self.JudgeSubTree(pRoot1.left, pRoot2.left)
    		else:
    			print "pRoot1.left.val: ",pRoot1.left.val
    			print "pRoot2.left.val: ",pRoot2.left.val
    			print "5"
    			return False
    	elif pRoot2.left==None:
    		print "6"
    		left =  True
    	elif pRoot2.left!=None and pRoot1.left==None:
    		print "7"
    		return False
    	if pRoot2.right!=None and pRoot1.right!=None:
    		if pRoot2.right.val==pRoot1.right.val:
    			right = self.JudgeSubTree(pRoot1.right, pRoot2.right)
    		else:
    			print "8"
    			return False
    	elif pRoot2.right==None:
    		print "9"
    		right =  True
    	elif pRoot2.right!=None and pRoot1.right==None:
    		print "10"
    		return False
    	print "11"
    	return left and right