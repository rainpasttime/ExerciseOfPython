from IsPopOrder import *
s = Solution()
a = [1,2,3,4,5]
b = [2,4,5,3,1]
print s.IsPopOrder(a,b)

a = [1,2,3,4,5]
b = [2,4,0,5,1]
print s.IsPopOrder(a,b)

a = [1,2,3,4,5]
b = [2,9,3,1,5]
print s.IsPopOrder(a,b)

a = [1,2,3,4,5]
b = [5,4,3,2,1]
print s.IsPopOrder(a,b)

a = [1,2,3,4,5]
b = [5,3,4,2,1]
print s.IsPopOrder(a,b)

a = [1,2,3,4,5]
b = [2,4,1,3,5]
print s.IsPopOrder(a,b)