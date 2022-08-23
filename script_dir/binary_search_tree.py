"构造二叉搜索树"

import random
# 树节点
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def __repr__(self):
    #     return 'Node({!r})'.format(self.value)


class BSTtree:
    def __init__(self, root=None, iterable=None):
        self.root = root
        self.iterable = iterable

    def search(self, node):
        if self.root == None:
            print('空树')
            return None,None
        current = self.root
        pre_cur = current
        while current != None:
            if current.value == node.value:
                print("节点已经存在")
                return (pre_cur,current) # 找到节点
            if current.value > node.value:
                pre_cur = current
                current = current.left
            else:
                pre_cur = current
                current = current.right

        return (pre_cur ,None)# 叶子节点

    def insert(self,node):
        "树中插入节点"
        pre,cur = self.search(node)
        if pre == None and cur == None:
            self.root = node
            print('构造一个新的树')
            return
        if cur != None:
            print('节点已经存在')
            return
        else:
            if pre.value > node.value:
                pre.left = node
            else:
                pre.right = node
        # print('插入一个节点')



# **********************************************************

    def min_node(self,node):
        "node 节点为根的子树的最小节点"
        if node == None:
            print('子树为空')
            return None
        cur = node
        while cur.left != None:
            pre = cur
            cur = cur.left
        return (pre,cur) #最小节点及父节点

    def max_node(self,node):
        "node 为根的子树最大节点"
        if node == None:
            print('子树为空')
            return
        cur = node
        while cur.right != None:
            pre = cur
            cur = cur.right
        return (pre,cur) # 最大节点及父节点

    def delete(self,node):
        "在树中删除一个节点"
        if node == None:
            return
        pre,cur = self.search(node)
        if cur == None:
            print('没有要删除的节点')
            return
        if cur.left == None or cur.right == None:
           if cur.left and pre.left == cur:
               pre.left = cur.left
           elif cur.right and pre.left == cur:
               pre.left = cur.right
           elif cur.left and pre.right == cur:
               pre.right = cur.left
           elif cur.right and pre.right == cur:
               pre.right = cur.right
           else:
               if pre.left == cur:
                   pre.left = None
               if pre.right == cur:
                   pre.right = None
           return
        else:
            right_min_p,right_min_c = self.min_node(cur.right)
            cur.value = right_min_c.value
            right_min_p.left = right_min_c.right
        # else:
        #     left_max_p,left_max_c = self.max_node(cur.left)
        #     cur.value = left_max_c.value
        #     left_max_p.right = left_max_c.left








    def built_tree(self):
        '''构造树'''
        if self.iterable == None:
            print('没有可构造的节点序列')
            return

        for value in self.iterable:
            node = Node(value)
            self.insert(node)

    def pre_traverse(self,node):
        "前序"
        cur = node
        if cur == None:
            return
        yield cur.value
        # print(cur.value,end = ',')
        yield from self.pre_traverse(cur.left)
        yield from self.pre_traverse(cur.right)

    def in_traverse(self,node):
        "中序"
        cur = node
        if cur == None:
            return
        yield from self.in_traverse(node.left)
        yield node.value
        yield from self.in_traverse(node.right)

    def post_traverse(self,node):
        "后序"
        cur = node
        if cur == None:
            return
        yield from self.post_traverse(node.left)
        yield from self.post_traverse(node.right)
        yield node.value

    def hier_traverse(self,node):
        "分层遍历"
        queue = []
        cur = node
        if cur == None:
            return
        queue.append(cur)
        while queue:
            temp = queue.pop(0)
            yield temp
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)






"实例化运行"
data = list(range(10))
random.shuffle(data)
print(data)
tree = BSTtree(None,data)
tree.built_tree()
tree.insert(Node(100))
tree.delete(Node(7))
in_iter = tree.in_traverse(tree.root)
# pre_iter = tree.pre_traverse(tree.root)
# post_iter = tree.post_traverse(tree.root)
# hier_iter = tree.hier_traverse(tree.root)
print(in_iter)
temp = []
for v in in_iter:
    temp.append(v)
print(temp)