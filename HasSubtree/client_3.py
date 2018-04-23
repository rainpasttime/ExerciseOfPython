from ListNode import *
from HasSubtree import *

s = Solution()

head_one = TreeNode(8)
tree_right = TreeNode(8)
head_one.right = tree_right

tree_right = TreeNode(9)
now = head_one.right
now.right = tree_right

tree_right = TreeNode(2)
now = now.right
now.right = tree_right

tree_right = TreeNode(5)
now = now.right
now.right = tree_right
# head_one.display()

head_two = TreeNode(8)
head_two.right = TreeNode(9)
now = head_two.right
now.right = TreeNode(2)
# head_two.display()

result = s.HasSubtree(head_one,head_two)
print result