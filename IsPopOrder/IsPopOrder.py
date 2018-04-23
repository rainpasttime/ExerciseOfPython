# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        #考虑相对位置
        if pushV==[] and popV==[]:
        	return True
        if len(pushV)==1 and len(popV)==1 and popV[0]==pushV[0]:
        	return True
        try:
        	index_one = pushV.index(popV[0])
        	index_two = pushV.index(popV[1])
        except Exception:
        	return False
        if index_one<index_two:
        	del pushV[index_one]
        	del popV[0]
        	return self.IsPopOrder(pushV,popV)
        elif index_two+1==index_one:
        	del pushV[index_one]
        	del popV[0]
        	return self.IsPopOrder(pushV,popV)
        else:
        	return False