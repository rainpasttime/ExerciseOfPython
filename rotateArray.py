# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
        	return 0
        else:
        	min = rotateArray[0]
        	for i in xrange(len(rotateArray)):
        		if min>rotateArray[i]:
        			min = rotateArray[i]
        	return min