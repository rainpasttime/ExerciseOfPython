# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
    	if len(sequence)==1:
    		return True
    	elif len(sequence)==0:
    		return False
    	else:
    		root = sequence[len(sequence)-1]
    		right = -1
    		for i in range(len(sequence)-1):
    			if sequence[i]>root:
    				right = i
    				break
    		if right!=-1:
    			for i in range(right+1,len(sequence)-1):
    				if sequence[i]<root:
    					return False
    			if right!=0:
    				left_flag = self.VerifySquenceOfBST(sequence[0:right])
    				right_flag = self.VerifySquenceOfBST(sequence[right:len(sequence)-1])
    				return left_flag and right_flag
    			else:
    				return self.VerifySquenceOfBST(sequence[right:len(sequence)-1])
    		else:
    			return self.VerifySquenceOfBST(sequence[0:len(sequence)-1])