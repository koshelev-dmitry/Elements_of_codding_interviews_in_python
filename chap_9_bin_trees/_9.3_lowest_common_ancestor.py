"""
lowest common ancestor = LCA
If two nodes are in a subtree
"""
import collections
def lca(tree, node_0, node_1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node_0, node_1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node_0, node_1)
        if left_result.num_target_nodes == 2:
            return left_result
        right_result = lca_helper(tree.right, node_0, node_1)
        if right_result.num_target_nodes == 2:
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes
            + int(tree is node_0) + int(tree is node_1))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    
    return lca_helper(tree, node_0, node_1).ancestor
