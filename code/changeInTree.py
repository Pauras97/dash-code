# Time and space O(M + N)
#Look below for detailed
class Node:
    def __init__(self, key, value, active):
        self.key = key
        self.value = value
        self.children = []
        self.isActive = active
    
    def equals(self, node):
        if not node:
            return False
        
        return self.key == node.key and self.value == node.value and self.isActive == node.isActive

def get_modified_items(t1, t2):
    if not t1 and not t2:
        return 0
    
    count = 0
    
    if not t1 or not t2 or not t1.equals(t2):
        count += 1
    
    child1 = getChildNodes(t1)
    child2 = getChildNodes(t2)
    
    for k in child1.keys():
        count += get_modified_items(child1.get(k), child2.get(k, None))
    
    for k in child2.keys():
        if k not in child1:
            count += get_modified_items(None, child2.get(k))
    
    return count

def getChildNodes(menu):
    table = {}
    if not menu:
        return table
    
    for node in menu.children:
        table[node.key] = node
    
    return table

a1 = Node("a", 1, True)
b1 = Node("b", 2, True)
c1 = Node("c", 3, True)
d1 = Node("d", 4, True)
e1 = Node("e", 5, True)
# f1 = Node("f", 6, True)
# g1 = Node("g", 7, True)
a1.children.append(b1)
a1.children.append(c1)
b1.children.append(d1)
b1.children.append(e1)
# c1.children.append(f1)
# c1.children.append(g1)

a2 = Node("a", 1, True)
b2 = Node("b", 2, True)
c2 = Node("c", 3, True)
d2 = Node("d", 4, True)
e2 = Node("e", 5, True)
# f2 = Node("f", 6, True)
# g2 = Node("g", 7, False)
a2.children.append(b2)
a2.children.append(c2)
b2.children.append(d2)
# b2.children.append(f2)
c2.children.append(e2)
# c2.children.append(g2)

# case 1 (without including commented code) - nodes changed are b and c; count = 2
# case 2 (after including commented code) - nodes changed are b, c, e, f and g; count = 5

print (get_modified_items(a1,a2))
        



T1 = Node('a', 1, True)
T1.children.append(Node('b', 2, True))
T1.children.append(Node('c', 3, True))
T1.children[0].children.append(Node('d', 4, True))
T1.children[0].children.append(Node('e', 5, True))
T1.children[1].children.append(Node('f', 6, True))

T2 = Node('a', 1, True)
T2.children.append(Node('c', 3, False))
T2.children[0].children.append(Node('f', 66, True))

print(get_modified_items(T1, T2))

T1 = Node('a', 1, True)
T1.children.append(Node('b', 2, True))
T1.children.append(Node('c', 3, True))
T1.children[0].children.append(Node('d', 4, True))
T1.children[0].children.append(Node('e', 5, True))
T1.children[1].children.append(Node('g', 7, True))

T2 = Node('a', 1, True)
T2.children.append(Node('b', 2, True))
T2.children.append(Node('c', 3, True))
T2.children[0].children.append(Node('d', 4, True))
T2.children[0].children.append(Node('e', 5, True))
T2.children[0].children.append(Node('f', 6, True))
T2.children[1].children.append(Node('g', 7, False))

print(get_modified_items(T1, T2))



# Given that the worst-case scenario involves comparing each node in tree 1 to every node in tree 2 (or vice versa),
# and that each node's children are also iterated over and compared, 
#the overall time complexity can be considered in terms of operations performed on each node and its children:

# For each node in tree 1, you potentially compare it with nodes in tree 2.
# You also generate child nodes maps for nodes in both trees and perform recursive comparisons.
# Thus, in the most straightforward analysis, assuming that you might have to visit and compare each node in one tree with each node in the other in the worst case,
#the time complexity would be proportional to the product of the number of nodes in each tree, i.e., 

# O(N×M). 
# However, due to the nature of the comparison (which does not actually compare every node in tree 1 with every node in tree 2 directly,
#but rather traverses the trees in a sort of parallel fashion), the practical time complexity is more nuanced and depends on the structure of the trees
# and how the nodes and their children are distributed.

# The real bottleneck comes from the iterations over the children of each node and the recursive calls made for these children.
#If we assume that the distribution of nodes is somewhat even and each node only makes a limited number of recursive calls to its children,
#the effective time complexity is closer to 
# O(N+M),
# because each node in both trees is processed at most once in the case of non-overlapping trees.

