from listNode import *
from ReverseList import *

head = ListNode(3)
s = head
for i in range(10):
	b = ListNode(i)
	s.next = b
	s = s.next
solution = Solution()
print solution.ReverseList(head).val
 