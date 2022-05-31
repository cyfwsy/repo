'''tree traverse'''
import pickle


class Node:
    ''' a simple digraph'''

    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        '''create a edge between this node and other'''
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)


def preorder_traversal(root, seen=None, parent=None):
    '''generator function to yield the edge in a graph'''
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)


def show_edge(root):
    '''print all the edge in the graph '''
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} --> {:>3} ({})'.format(parent.name, child.name, id(child)))


# setup node and edge
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)
print('Original graph')
show_edge(root)

# pickle and unpickle
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\n reloaded graph')
show_edge(root)
