# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in range(len(array)):
        	if array[i]%2==0:
        		even.append(array[i])
        	else:
        		odd.append(array[i])
        return odd+even