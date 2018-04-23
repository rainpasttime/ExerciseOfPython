# -*- coding:utf-8 -*-
from Mirror import *
from TreeNode import *

head_one = TreeNode(8)
head_one.left = TreeNode(6)
head_one.right = TreeNode(10)

now = head_one.left
now.left = TreeNode(5)
now.right = TreeNode(7)

now = head_one.right
now.left  = TreeNode(9)
now.right = TreeNode(11)

mirror = Solution()
result = mirror.Mirror(head_one)
result.display()