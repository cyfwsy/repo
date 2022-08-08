'广度优先算法'
from collections import deque


def bfs(graph, start=0):
    to_visit = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:
        node = to_visit.pop()
        print('----->>>  {}'.format(node))
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec


def prec_node_map(prec, start):
    "create a mapping node to post_node list"
    map_node = {}
    for i in range(len(prec)):
        map_node[i] = []
    for i in prec:
        if i == None:
            map_node['None'] = [start]
        else:
            for j in range(len(prec)):
                if prec[j] == i:
                    map_node[int(i)].append(j)
    for i in map_node.keys():
        map_node[i] = set(map_node[i])
    return map_node


graph_1 = [[1, 4], [0, 5], [3, 5], [2, 6], [0, 5, 6], [1, 2, 4], [3, 4]]
dist, prec = bfs(graph_1, start=5)
print(dist)
print(prec)
print(prec_node_map(prec, 5))
