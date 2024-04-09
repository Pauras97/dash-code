# A dasher sometimes travels between cities. To avoid delays, the dasher first checks for the shortest routes.
#Given a map of the cities and their bidirectional roads represented by a graph of nodes and edges, determine which given roads are along any shortest path.
#Return an array of strings, one for each road in order, where the value is YES if the road is along a shortest path or NO if it is not.
#The roads or edges are named using their 1-based index within the input array



from collections import deque
def find_shortest_paths_2(node_g, src, dest, weight):
    graph = defaultdict(list)
    for i in range(len(src)):
        s, d = src[i], dest[i]
        graph[s].append(i)
        graph[d].append(i)
    
    allMinPath = set()
    minDist = float('inf')
    queue = deque([(1, 0, set())])
    
    while queue:
        city, dist, visited = queue.popleft()
        
        if city == node_g:
            if dist < minDist:
                minDist = dist
                allMinPath = set()
            allMinPath = allMinPath | visited
        
        if dist < minDist:
            for edgeIdx in graph[city]:
                if edgeIdx not in visited:
                    if dest[edgeIdx] == city:
                        queue.append((src[edgeIdx], dist + weight[edgeIdx], visited | {edgeIdx}))
                    else:
                        queue.append((dest[edgeIdx], dist + weight[edgeIdx], visited | {edgeIdx}))
    
    ans = ["NO"] * len(src)
    for idx in allMinPath:
        ans[idx] = "YES"
    
    return ans
       
        
if __name__ == '__main__':
    ans = find_shortest_paths_2(
        5,
        [1, 2, 3, 4, 5, 1, 5],
        [2, 3, 4, 5, 1, 3, 3],
        [1, 1, 1, 1, 3, 2, 1]
    )
    print(ans)




# Example
# given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:

# Road from/to/weight
# 1 (1, 2, 1)
# 2 (2, 3, 1)
# 3 (3, 4, 1)
# 4 (4, 5, 1)
# 5 (5, 1, 3)
# 6 (1, 3, 2)
# 7 (5, 3, 1)

# Example Input: (5, [1, 2, 3, 4, 5, 1, 5], [
# 2, 3, 4, 5, 1, 3, 3], [1, 1, 1, 1, 3, 2, 1])
# The traveller must travel from city 1 to city g_nodes, so from node 1 to node 5 in this case.
# The shortest path is 3 units long and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.
# Return an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. In this case, the resulting array is ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES']. The third and fourth roads connect nodes (3, 4) and (4, 5) respectively. They are not on a shortest path, i.e. one with a length of 3 in this case.