def dfs_recursive(graph,node,seen):
    seen[node] = True
    print(node,end=',')
    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs_recursive(graph,neighbor,seen)
            
graph_1 = [[1, 4], [0, 5], [3, 5], [2, 6], [0, 5, 6], [1, 2, 4], [3, 4]]
seen = []
for i in range(len(graph_1)):
    seen.append(False) 
print(seen)
dfs_recursive(graph_1,3,seen)
