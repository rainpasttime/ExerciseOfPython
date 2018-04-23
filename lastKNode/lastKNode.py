# -*- coding:utf-8 -*-
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        array = []
        iterator = head
        while iterator!=None:
        	array.append(iterator.val)
        	iterator = iterator.next
        if k > len(array):
        	return False
        elif k<1:
        	return False
        else:
        	return array[-k]