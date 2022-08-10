"用迭代方法遍历图"
def dfs_iterative(graph,start,seen):
    seen[start] = True
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        print(node,end=',')
        for neighbor in graph[node]:
            if not seen[neighbor]:
                seen[neighbor] = True
                to_visit.append(neighbor)
                
graph_1 = [[1, 4], [0, 5], [3, 5], [2, 6], [0, 5, 6], [1, 2, 4], [3, 4]]
seen = [False] * len(graph_1)
dfs_iterative(graph_1,5,seen)
