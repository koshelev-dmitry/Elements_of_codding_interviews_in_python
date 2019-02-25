import collections

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))
    
    def check_balance(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        
        left_result = check_balance(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balance(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)
    
        is_balanced = abs(right_result.height - left_result.height) <= 1
        height = max(right_result.height, left_result.height)
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balance(tree).balanced