# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        size_one = len(matrix)
        size_two = len(matrix[0])
        if size_one>size_two:
    		if size_two%2==1:
    			count = (size_two+1)/2
    		else:
    			count = size_two/2
    	else:
    		if size_one%2==1:
    			count = (size_one+1)/2
    		else:
    			count = size_one/2
        self.output(result,matrix,0,size_one,size_two,count)
        return result

    def output(self,result,matrix,n,size_one,size_two,count):
    	for i in range(0,size_two):
    		result.append(matrix[n][n+i])
    	for i in range(n+1,n+size_one):
    		result.append(matrix[i][n+size_two-1])
    	if n!=n+size_two-1 and n!=n+size_one-1:
    		for i in range(2,size_two+1):         
    			result.append(matrix[n+size_one-1][n+size_two-i])
    		for i in range(2,size_one):                   ##
    			result.append(matrix[n+size_one-i][n])
    	if n+1<count:
    		self.output(result,matrix,n+1,size_one-2,size_two-2,count)