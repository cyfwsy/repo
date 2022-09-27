import pickle
class Node:
    # a simple digraph
    def __init__(self,name):
        self.name = name
        self.connections = []
        
    def add_edge(self,node):
        self.connections.append(node)
        
    def __iter__(self):
        return iter(self.connections)
    
def preorder_traversal(root,seen=None,parent=None):
    # generator function to yield the edges in a graph
    if seen is None:
        seen = set()
    yield (parent,root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node,seen,root)
        for parent,subnode in recurse:
            yield (parent,subnode)
            
def show_edges(root):
    # print all edges in the graph
    for parent,child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5}--->{:>2} ({})'.format(\
            parent.name,child.name,id(child)))
        
root = Node('root') #set up nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

# add edges between nodes
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
c.add_edge(e)
c.add_edge(f)
c.add_edge(g)
g.add_edge(f)
g.add_edge(h)
g.add_edge(root)
h.add_edge(root)

# print original graph 
show_edges(root)

# pickle and unpickle to create a new set of nodes
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

# print reloaded graph
show_edges(reloaded)





