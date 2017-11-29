#!/bin/python3

import sys

def main(argv):
	
	print ("Creating bin tree")

	tree = createBinaryTreeManually()
	
	#print(str(tree))

	print("Doing : inorder_tree_traversal")
	inorder_tree_traversal(tree)
	print('\n')

def inorder_tree_traversal(root):
	
	if root:
		inorder_tree_traversal(root.left)
		sys.stdout.write("{},".format(root.data))
		inorder_tree_traversal(root.right)

# Tree on Fig 9.1, pg 113
def createBinaryTreeManually():
	
	leaf_1 = Btn(641)
	leaf_2 = Btn(257)
	leaf_3 = Btn(17)
	leaf_4 = Btn(28)
	leaf_5 = Btn(28)
	leaf_6 = Btn(0)

	d4_1 = Btn(401,None,leaf_1)
	
	d3_1 = Btn(3, leaf_3, None)
	d3_2 = Btn(1, d4_1, leaf_2)

	d2_1 = Btn(271, leaf_4,leaf_6)
	d2_2 = Btn(561, None, d3_1)
	d2_3 = Btn(2, None,d3_2)
	d2_4 = Btn(271,None,leaf_5)

	d1_1 = Btn(6,d2_1, d2_2)
	d1_2 = Btn(6,d2_3, d2_4)

	d0 = Btn(314, d1_1, d1_2)
	
	
	return d0

#Binary tree node
class Btn():

	def __init__(self, node_data, left_node=None, right_node=None):

		self.data = node_data
		self.left = left_node
		self.right = right_node
	
	def __str__(self):

		return str(self.data)

if __name__ == "__main__":main(sys.argv[0:])
