'''实现 自定义容器，用内置类容器做基类'''
from collections.abc import Sequence,Iterable
import random

class BinaryNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            for i in self.left._traverse():
                yield i
        yield self
        if self.right is not None:
            for i in self.right._traverse():
                yield i
    def __getitem__(self, index):
        for i ,item  in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')

class SequenceNode(IndexableNode):
    def __len__(self):
        for count,_ in enumerate(self._traverse,1):
            pass
        return count


root = SequenceNode(7)
n1 = SequenceNode(8)
n2 = SequenceNode(20)
n3 = SequenceNode(33)
n4 = SequenceNode(100)
n5 = SequenceNode(99)
n6 = SequenceNode(301)
n8 = SequenceNode(270)
n9 = SequenceNode(2)
n10 = SequenceNode(78)
root.left = n1
root.right = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n6.left = n8
n6.right = n9
n8.right = n10
for i in root:
    print(i)
print(root)



