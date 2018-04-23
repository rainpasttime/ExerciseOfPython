from TreeNode import *
from rebuildTree import *

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

s = Solution()
output = s.reConstructBinaryTree(pre, tin)

output.display_pre()

print "\n\n"

output.display_tin()