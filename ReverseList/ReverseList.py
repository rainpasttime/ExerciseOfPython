# -*- coding:utf-8 -*-
#反转链表并输出链表的元素
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        iterator_pre = pHead
        iterator_mid = pHead.next
        iterator_next = pHead.next.next
        pHead.next = None
        while iterator_mid!=None:
        	iterator_mid.next = iterator_pre
        	iterator_pre = iterator_mid
        	iterator_mid = iterator_next
        	if iterator_next!=None:
        		iterator_next = iterator_next.next
        return iterator_pre