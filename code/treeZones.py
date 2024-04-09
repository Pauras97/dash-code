def getHighestScore(parents):
    graph = defaultdict(list)
    
    for node, parent in enumerate(parents):
        graph[parent].append(node)
    
    freq = Counter()
    n = len(parents)
    
    def dfs(node):
        left = right = 0
        
        if graph[node]:
            left = dfs(graph[node][0])
        if len(graph[node]) > 1:
            right = dfs(graph[node][1])
        
        up = n - left - right - 1
        score = (left or 1) * (right or 1) * (up or 1)
        freq[score] += 1
        return 1 + left + right
            
    dfs(0)
    return freq[max(freq.keys())]

parents = [-1,2,0,2,0]
print(getHighestScore(parents))
parents = [-1,2,0]
print(getHighestScore(parents))
parents = [-1, 0, 0]
print(getHighestScore(parents))

# DESC 1
# There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. 
#You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

# Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed.
#The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it.
#The score of the node is the product of the sizes of all those subtrees.

# Return the number of nodes that have the highest score.


# DESC2
# You have a binary tree of zones, represented as a list of numbers which has the parents of each node
#(index is the node, and the value in the list is the parent of that particular node). 
#E.g., if the list is [-1, 0, 0] -> the parent of node 0 is -1 (as it is a root node), parent of node 1 and node 2 both are 0.
#The root zone has value 0, and all values are +ve integers. Remove one edge each time.
#The value of each zone is product of values of all nodes in that region. Return the number of nodes when the entire tree has the most optimized value.