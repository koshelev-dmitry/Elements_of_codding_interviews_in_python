def find_k_largest_elements_BST(tree, k):
    def inorder_walk_helper(tree):
        if tree and len(result) < k:
            inorder_walk_helper(tree.right)
            if len(result) < k:
                result.append(tree.val)
                inorder_walk_helper(tree.left)

    result = []
    inorder_walk_helper(tree)
    return result
    