from ListNode import *
from HasSubtree import *

s = Solution()

head_one = TreeNode(8)
tree_left = TreeNode(8)
head_one.left = tree_left

tree_left = TreeNode(9)
now = head_one.left
now.left = tree_left

tree_left = TreeNode(2)
now = now.left
now.left = tree_left

tree_left = TreeNode(5)
now = now.left
now.left = tree_left
# head_one.display()

head_two = TreeNode(8)
head_two.left = TreeNode(9)
now = head_two.left
now.left = TreeNode(3)
# head_two.display()

result = s.HasSubtree(head_one,head_two)
print result