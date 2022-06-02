'''bellman_ford 算法'''
import sys


def bellman_ford(s,vertex_list,edges):
    distance = {}
    for v in vertex_list:# 将起始节点与其他节点的距离设为无穷大
        if v == s:
            distance[(s,v)] = 0
        else:
            distance[(s,v)] = sys.maxsize
    for i in range(len(vertex_list)):# 外层循环，顶点数量
        for edge in edges.keys():# 内层循环，边数量
            u = edge[0]
            v = edge[1]
            if distance[(s,u)] < sys.maxsize and distance[(s,u)] + edges[edge] \
                < distance[(s,v)]:
                distance[(s,v)] = distance[(s,u)] + edges[edge]
                print('from {0} to {1} then to {2} can be shorter with distance{3}'.\
                      format(s,u,v,distance[(s,v)]))
    for edge in edges.keys():# 检测是否有负环发生
        u = edge[0]
        v = edge[1]
        if distance[(s,v)] > distance[(s,u)] + edges[edge]:
            return None
    return distance

vertex_list = ['A','B','C','D','E','F']
edges = {} #记录边长度
edges[('A','B')] = 10
edges[('A','E')] = 3
edges[('B','C')] = 2
edges[('B','F')] = -3
edges[('C','B')] = -1
edges[('E','F')] = 3
edges[('F','C')] = 4
edges[('F','D')] = 1
edges[('D','C')] = 4

distances = bellman_ford('A',vertex_list,edges)
for d in distances.keys():
    print('the shortest path from A to {0} is {1}'.format(d[1],distances[d]))




