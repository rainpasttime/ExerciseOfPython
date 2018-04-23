from ListNode import *
from HasSubtree import *

s = Solution()

head_one = TreeNode(8)
tree_left = TreeNode(8)
tree_right = TreeNode(7)
head_one.left = tree_left
head_one.right = tree_right

tree_left = TreeNode(9)
tree_right = TreeNode(2)
now = head_one.left
now.left = tree_left
now.right = tree_right

tree_left = TreeNode(4)
tree_right = TreeNode(7)
now = now.right
now.left = tree_left
now.right= tree_right

# head_one.display()


head_two = TreeNode(8)
head_two.left = TreeNode(9)
head_two.right = TreeNode(2)
# head_two.display()

result = s.HasSubtree(head_one,head_two)
print result