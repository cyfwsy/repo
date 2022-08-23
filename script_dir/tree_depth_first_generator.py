"树结构生成器例子"

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    child2.add_child(Node(6))
    child2.add_child(Node(7))
    child2.add_child(Node(8))
    child3 = Node(8)
    child2.add_child(Node(8))
    child2.add_child(Node(9))
    child2.add_child(Node(11))
    child3.add_child(Node(10))
    

    for ch in root.depth_first():
        print(ch)