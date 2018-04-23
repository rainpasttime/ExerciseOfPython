class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def display_pre(self):
    	print self.val
    	if self.left!=None:
    		self.left.display_pre()
    	if self.right!=None:
    		self.right.display_pre()
    def display_tin(self):
    	if self.left!=None:
    		self.left.display_tin()
    	print self.val
    	if self.right!=None:
    		self.right.display_tin()