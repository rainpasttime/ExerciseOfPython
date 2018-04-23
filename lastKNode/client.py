from listNode import *
from lastKNode import *

head = ListNode(3)
s = head
for i in range(10):
	b = ListNode(i)
	s.next = b
	s = s.next
solution = Solution()
print solution.FindKthToTail(head,3)
print solution.FindKthToTail(head,6)
print solution.FindKthToTail(head,19)
print solution.FindKthToTail(head,2)