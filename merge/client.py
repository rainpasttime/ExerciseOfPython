from listNode import *
from merge import *
print "head_one: "
head_one = ListNode(5)
print head_one.val
iterator = head_one
for i in range(20):
	node = ListNode(17+5*i)
	print node.val
	iterator.next = node
	iterator = iterator.next

print "head_two: "
head_two = ListNode(3)
print head_two.val
iterator = head_two
for i in range(17):
	node = ListNode(7+3*i)
	print node.val
	iterator.next = node
	iterator = iterator.next
s = Solution()
result = s.Merge(head_one,head_two)
iterator = result
print "result: "
while iterator!=None:
	print iterator.val
	iterator = iterator.next