class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
def count_differences_revised(node1, node2):
    if not node1 and not node2:
        return 0
    if not node1 or not node2:
        # Count all nodes in the non-None tree
        return sum(1 + len(node.children) for node in (node1.children if node1 else node2.children)) + 1

    diff = 0
    if node1.key != node2.key:
        # Different keys, count all children as differences too
        diff += 1 + len(node1.children) + len(node2.children)
    elif node1.value != node2.value:
        # Same key but different value
        diff += 1

    # If keys are the same, compare children regardless of values
    if node1.key == node2.key:
        # Create mappings based on keys for easier comparison
        children1 = {child.key: child for child in node1.children}
        children2 = {child.key: child for child in node2.children}

        for key in set(children1.keys()).union(set(children2.keys())):
            diff += count_differences_revised(children1.get(key), children2.get(key))

    return diff

T1 = Node('a', 1)
T1.children.append(Node('b', 2))
T1.children.append(Node('c', 3))
T1.children[0].children.append(Node('d', 4))
T1.children[0].children.append(Node('e', 5))
T1.children[1].children.append(Node('f', 6))

T2 = Node('a', 1)
T2.children.append(Node('c', 3))
T2.children[0].children.append(Node('f', 66))

print(count_differences_revised(T1, T2))

T1 = Node('a', 1)
T1.children.append(Node('b', 2))
T1.children.append(Node('c', 3))
T1.children[0].children.append(Node('d', 4))
T1.children[0].children.append(Node('e', 5))
T1.children[1].children.append(Node('g', 7))

T2 = Node('a', 1)
T2.children.append(Node('b', 2))
T2.children.append(Node('h', 8))
T2.children[0].children.append(Node('d', 4))
T2.children[0].children.append(Node('e', 5))
T2.children[0].children.append(Node('f', 6))
T2.children[1].children.append(Node('g', 7))

print(count_differences_revised(T1, T2))


# Compare the two trees and calculate how many nodes have changed

# Example 1
#            Existing tree                                       
#               a(1)                                               
#            /       \                                                         
#         b(2)       c(3)                                              
#        /     \         \                                                        
#      d(4)    e(5)      f(6)     
    
#                  New tree
#            a(1)
#                \
#               c(3)
#                   \
#                   f(66)
                  
#    Expected answer: 4 
#    (Three extra nodes in first tree and f6 != f66)


# Example 2
#          Existing tree                                                  
#            a(1)                                                
#          /       \                                                
#        b(2)      c(3)                                  
#      /       \       \                                         
#  d(4)      e(5)      g(7)   
 
#                New tree
#                a(1)
#            /        \                                                                
#         b(2)         h(8) 
#      /    |   \           \   
# e(5)   d(4)   f(6)       g(7)

# Expected answer: 5
# c3 != h8 so the subtree c(3) -> g(7) != h(8) -> g(7) so +4, f6 is an addition so +1. 

# I believe if key is same and value is different there is a +1 difference but if both are different it's a +2 difference (since they are different nodes)
# The order of the direct child nodes do not matter when comparing two trees