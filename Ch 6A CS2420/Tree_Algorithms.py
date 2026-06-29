from Algo_and_Struts_06_i_tree_node import TreeNode

def numberOfLeaves(n :TreeNode) -> int:
	#count & return num of leaves listed in tree
	if n is None:
		return 0
	if n.left_child is None and n.right_child is None:
		return 1
	
	return numberOfLeaves(n.left_child) + numberOfLeaves(n.right_child)
    
def numberOfNodesWithASingleChild(n :TreeNode)  -> int:
	#count & return num of tree nodes that only have
	#a single child in the provided tree
	if n is None:
		return 0
	i = numberOfNodesWithASingleChild(n.left_child) + numberOfNodesWithASingleChild(n.right_child)
	
	if (n.left_child is None and n.right_child is not None) or (n.left_child is not None and n.right_child is None):
		return 1 + i
	else:
		return i
	#return -1

def numberOfNodesWithTwoChildren(n :TreeNode)  -> int:
	#count & return num of tree nodes that have
	#2 children in the provided tree
	if n is None:
		return 0
	j = numberOfNodesWithTwoChildren(n.left_child) + numberOfNodesWithTwoChildren(n.right_child)
	
	if n.has_children():
		return 1 + j
	else:
		return j
	#return -1
	
def numberOfNodesWithEvenDataItems(n :TreeNode)  -> int:
    #count & return num of tree nodes that have
    #even values in the provided tree
    if n is None:
        return 0

    k = numberOfNodesWithEvenDataItems(n.left_child) + numberOfNodesWithEvenDataItems(n.right_child)
    #check if even (w/ value NOT key)
    if n.value % 2 == 0:
        return 1 + k
    else:
        return k
    #return -1

def sumOfAllItems(n :TreeNode)  -> int:
	#count & return all values in the provided tree
	#m = sumOfAllItems(n.left_child) + sumOfAllItems(n.right_child)

	if n is None:
		return 0
	m = sumOfAllItems(n.left_child) + sumOfAllItems(n.right_child)
	return n.value + m
	#return -1

def printRuntimes():
    #TODO type in the runtimes on these lines: i.e. log(n), n, n log(n), n*n, etc
    print("BigOh runtime of numberOfLeaves is: O(n)")
    print("BigOh runtime of numberOfNodesWithOneNonNullChild is: O(n)")
    print("BigOh runtime of numberOfNodesWithTwoNonNullChildren is: O(n)")
    print("BigOh runtime of numberOfNodesWithEvenDataItems is: O(n)")
    print("BigOh runtime of sumOfAllItems is: O(n)")
		