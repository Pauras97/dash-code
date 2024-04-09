class Node:
    # Binary Tree Node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.isActive = True

## ANY MAXIMUM PATH SUM
def maxPathSum1(root: Optional[Node]) -> int:
    def helper(node):
        if not node:
            return 0

        nonlocal maxSum

        leftMax = helper(node.left)
        rightMax = helper(node.right)

        maxOneSide = max(node.val, max(leftMax, rightMax) + node.val)
        maxSubTree = max(maxOneSide, node.val + leftMax + rightMax)
        maxSum = max(maxSum, maxSubTree)
        return maxOneSide

    maxSum = float('-inf')
    helper(root)
    return maxSum
        
## Must HAVE LEAVES
def maxPathSum2(root: Node) -> int:
    def dfs(root):
        if not root:
            return float('-inf')  # Base case for null nodes.

        if not root.left and not root.right:
            return root.val  # Base case for leaf nodes.

        nonlocal maxSum

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        # Since we're looking for max path sum specifically between two leaves,
        # we update maxSum only if both children exist, indicating a path through root.
        if root.left and root.right:
            maxSum = max(maxSum, root.val + leftMax + rightMax)

        # Return the maximum sum of the path ending at this node going upwards.
        return root.val + max(leftMax, rightMax)

    maxSum = float('-inf')
    dfs(root)
    return maxSum

## MUST HAVE LEAVES NODES AND ALL NODES SHOULD BE ACTIVE
def maxPathSum3(root: Node) -> int:
    def dfs(root):
        # If the node is null or not active, treat it as if it doesn't exist for path calculations
        if not root or not root.isActive:
            return float('-inf'), False

        # Base case for leaf nodes.
        if not root.left and not root.right:
            return root.val, True

        leftMax, leftActive = dfs(root.left)
        rightMax, rightActive = dfs(root.right)

        # Compute maxSum if both children are active, or at least one active path exists through the node.
        if leftActive and rightActive:
            maxSum[0] = max(maxSum[0], root.val + leftMax + rightMax)
            return max(leftMax, rightMax) + root.val, True
        elif leftActive:
            return leftMax + root.val, True
        elif rightActive:
            return rightMax + root.val, True
        else:
            return float('-inf'), False

    maxSum = [float('-inf')]
    _, isActive = dfs(root)
    return maxSum[0] if isActive else 0


#MUST HAVE LEAVES AND ONLY LEAF NODES ACTIVE
def maxPathSum4(root: Node) -> int:
    def dfs(root):
        if not root:
            return float('-inf'), False

        # Check isActive only for leaf nodes
        if not root.left and not root.right:
            return (root.val, True) if root.isActive else (float('-inf'), False)

        leftMax, leftLeafActive = dfs(root.left)
        rightMax, rightLeafActive = dfs(root.right)

        # Update maxSum considering only active leaf conditions
        if leftLeafActive and rightLeafActive:
            maxSum[0] = max(maxSum[0], root.val + leftMax + rightMax)

        # No need to check isActive for non-leaf nodes
        return root.val + max(leftMax, rightMax), True

    maxSum = [float('-inf')]
    dfs(root)
    return maxSum[0]


## ANY PATH BUT NODES SHOULD BE ACTIVE
def maxPathSum5(root: Optional[Node]) -> int:
    def helper(node):
        # If the node is null or not active, return the lowest possible number
        if not node or not node.isActive:
            return float('-inf')
        
        nonlocal maxSum
        
        # Compute the max path sum recursively for left and right children
        leftMax = helper(node.left)
        rightMax = helper(node.right)
        
        # Calculate the maximum path sum considering the current node
        # Ensure to consider only paths that include the current node by checking for negative values and replacing them with 0
        maxThroughRoot = node.val + max(0, leftMax) + max(0, rightMax)
        
        # Update the global maximum path sum
        maxSum = max(maxSum, maxThroughRoot)
        
        # Return the maximum sum of a path passing through the current node, but only one side (left or right)
        return node.val + max(0, leftMax, rightMax)

    maxSum = float('-inf')
    helper(root)
    return maxSum

'''
       1
   2         3
         4(F)   5
'''
T1 = Node(1)
T1.left = Node(2)
T1.right = Node(3)
T1.right.left = Node(4)
T1.right.left.isActive = False
T1.right.right = Node(5)
'''
       1
 2(F)       -3
         -4   -5
'''
T2 = Node(1)
T2.left = Node(2)
T2.left.isActive = False
T2.right = Node(-3)
T2.right.left = Node(-4)
T2.right.right = Node(-5)

'''
       -5
   5        5
         5(F)   5
'''
T3 = Node(-5)
T3.left = Node(5)
T3.right = Node(5)
T3.right.left = Node(5)
T3.right.left.isActive = False
T3.right.right = Node(5)

'''
       -5
   -3     10(F)
        -3  -6(F)
'''
T4 = Node(-5)
T4.left = Node(-3)
T4.right = Node(10)
T4.right.isActive = False
T4.right.left = Node(-3)
T4.right.right = Node(-6)
T4.right.right.isActive = False

'''
       -5
   -3     10
'''
T5 = Node(-5)
T5.left = Node(-3)
T5.right = Node(10)


tests = [
    [T1, 12],
    [T2, 2],
    [T3, 15],
    [T4, 1],
    [T5, 10],
]

for n, t in enumerate(tests):
    print("PARENTS as well ", maxPathSum1(t[0]))
    res = maxPathSum2(t[0])
    print('TEST {} | actual={}, expected={}'.format(n + 1, res, t[1]))
    print("ACTIVE LEAVES ALL NODEs", maxPathSum3(t[0]))
    print("ACTIVE LEAVES ONLY", maxPathSum4(t[0]))
    print("PARENTS AND ACITVE ", maxPathSum5(t[0]))
    print("")