class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)

class Solution:
	def flatten(self, root):
		temp = root
		printTree(temp)
		print('\n')
		if temp is not None:
			if temp.left is not None:
				right = temp.right
				temp.right = temp.left
				temp.left = None
				temp = temp.right
				self.append(temp, right)
				self.flatten(temp)
			else:
				self.flatten(temp.right)

	def append(self, root, node):
		if root is None:
			return None
		if root.right is None:
			root.right = node
		else:
			self.append(root.right, node)

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
s = Solution()
s.flatten(root)
printTree(root)