# -*- coding:utf-8 -*-
from TreeNode import *
from PrintFromTopToBottom import *

s = Solution()

head_one = TreeNode(3)
print s.PrintFromTopToBottom(head_one)

print s.PrintFromTopToBottom(None)

left = TreeNode(4)
left.left = TreeNode(5)
left.right = TreeNode(3)
head_two = TreeNode(1)
head_two.left = left
head_two.right = TreeNode(2)
print s.PrintFromTopToBottom(head_two)

