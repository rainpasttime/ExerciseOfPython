#-*- coding:utf-8 -*-
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead2==None:
        	return pHead1
        elif pHead1==None:
        	return pHead2
        elif pHead2.val<pHead1.val:
        	result = pHead2
        	tail = result
        	iterator_one = pHead1
        	iterator_two = pHead2.next
        else:
        	result = pHead1
        	tail = result
        	iterator_one = pHead1.next
        	iterator_two = pHead2
        while iterator_one!=None and iterator_two!=None:
        	if iterator_one.val<iterator_two.val:
        		tail.next = iterator_one
        		tail = iterator_one
        		iterator_one = iterator_one.next
        	else:
        		tail.next = iterator_two
        		tail = iterator_two
        		iterator_two = iterator_two.next
        if iterator_one!=None:
        	tail.next = iterator_one
        	tail = iterator_one
        	iterator_one = iterator_one.next
        if iterator_two!=None:
        	tail.next = iterator_two
        	tail = iterator_two
        	iterator_two = iterator_two.next
        return result