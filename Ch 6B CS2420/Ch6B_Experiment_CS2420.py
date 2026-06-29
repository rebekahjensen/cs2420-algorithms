import random
import time
import tail_recursion
from binary_search_tree import BinarySearchTree, BinaryTreeNode
from avl_tree import AVLTree, AVLTreeNode

#inserting
def test_inserting(tree, data):
    start_time = time.time()
    for value in data:
        tree.put(value, None)
    return time.time() - start_time

#searching
def test_searching(tree, data):
    start_time = time.time()
    for value in data:
        tree.get(value)
    return time.time() - start_time

#run for bst & avl
def run_experiment():
    items_test = [1000, 10000, 100000, 10000000]
    results = {"Binary Search Tree": {"sorted_insertion": [], "random_insertion": [], "search": []},
    "AVL Tree": {"sorted_insertion": [], "random_insertion": [], "search": []}}

    for size in items_test:
        print(f"Testing experiment for size {size}")

        #create sorted data
        sorted_data = list(range(size))
        #create random data
        random_data = random.sample(range(size), size)

        #BST
        bst_sorted = BinarySearchTree()
        bst_random = BinarySearchTree()

        print("Testing Binary Search Tree")
        sorted_insert_time = test_inserting(bst_sorted, sorted_data)
        random_insert_time = test_inserting(bst_random, random_data)
        search_values = random.sample(random_data, min(1000, size))
        search_time = test_searching(bst_random, search_values)
        
        results["Binary Search Tree"]["sorted_insertion"].append(sorted_insert_time)
        results["Binary Search Tree"]["random_insertion"].append(random_insert_time)
        results["Binary Search Tree"]["search"].append(search_time)

        print(f"Binary Search Tree (sorted): {sorted_insert_time:.6f} seconds")
        print(f"Binary Search Tree (random): {random_insert_time:.6f} seconds")
        print(f"Binary Search Tree (search): {search_time:.6f} seconds")

        #AVL tree
        avl_sorted = AVLTree()
        avl_random = AVLTree()

        print("Testing AVL Tree")
        sorted_insert_time = test_inserting(avl_sorted, sorted_data)
        random_insert_time = test_inserting(avl_random, random_data)
        # search_values = random.sample(random_data, min(1000, size))
        search_time = test_searching(avl_random, search_values)

        results["AVL Tree"]["sorted_insertion"].append(sorted_insert_time)
        results["AVL Tree"]["random_insertion"].append(random_insert_time)
        results["AVL Tree"]["search"].append(search_time)

        print(f"AVL Tree (sorted): {sorted_insert_time:.6f} seconds")
        print(f"AVL Tree (random): {random_insert_time:.6f} seconds")
        print(f"AVL Tree (search): {search_time:.6f} seconds")

    return results

if __name__ == "__main__":
    results = run_experiment()
    