# -*- coding:utf-8 -*-
from TreeNode import *
from FindPath import *

head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(2)
head.right = TreeNode(3)
head.right.right = TreeNode(1)

s = Solution()
print s.FindPath(head,5)

print s.FindPath(None,4)