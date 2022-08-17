# A recursive generator that generates Tree leaves in in-order.
from __future__ import print_function


def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t

        for x in inorder(t.right):
            yield x
            
class bi_tree():
    def __init__(self,label,left=None,right=None):
        self.label = label
        self.left = left
        self.right = right
        
t1 = bi_tree('root')
t2 = bi_tree('a')
t3 = bi_tree('b')
t4 = bi_tree('c')
t5 = bi_tree('d')
t6 = bi_tree('e')
t7 = bi_tree('f')
t8 = bi_tree('g')
t9 = bi_tree('h')
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5
t4.left = t6
t4.right = t7
t5.left = t8
t5.right = t9

t_gen = inorder(t1)
print(t_gen)
for node in t_gen:
    print(node.label)
