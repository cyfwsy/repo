'广度优先算法'
from collections import deque
def bfs(graph,start=0):
    to_visit = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:
        node = to_visit.pop()
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist,prec

graph_1 = [[1,4],[0,5],[3,5],[2,6],[0,5,6],[1,2,4],[3,4]]
dist,prec = bfs(graph_1)
print(dist)
print(prec)
    