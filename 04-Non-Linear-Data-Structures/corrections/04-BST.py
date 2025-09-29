from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(preorder):
    def helper(lower=float('-inf'), upper=float('inf')):
        nonlocal idx;
        if idx == n:
            return None
        
        val = preorder[idx]
        if val < lower or val > upper:
            return None
        
        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root;

    idx = 0
    n = len(preorder)
    return helper()

def tree_to_list(root):
    if not root:
        return []
    
    result = [];
    queue = deque([root])

    while queue:
        node = queue.popleft();
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop();

    return result;

root = bstFromPreorder([8,5,1,7,10,12])

print(tree_to_list(root))



