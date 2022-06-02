'''实现非递归的访问者模式，数据结构类型和各种访问方法独立分离'''
import types
import sys
class Node:
    pass
class NodeVisitor:
    def visit(self,node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last,types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last,Node):
                    stack.append((self._visit(stack.pop())))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self,node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self,methname,None)
        if meth is None:
            meth = self.generic_visit(self,node)
        return meth(node)

    def generic_visit(self,node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class UnaryOperator(Node):
    def __init__(self,operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self,value):
        self.value = value

#A sample visitor class that evaluates expressions
class Evaluator(NodeVisitor):
    def visit_Number(self,node):
        return node.value

    def visit_Add(self,node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self,node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self,node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self,node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self,node):
        yield -(yield node.operand)
# 
#使用递归的方法运行，可能系统栈溢出，系统崩溃 很容易就超过递归深度
# class Evaluator(NodeVisitor):
#     def visit_Number(self,node):
#         return node.value
#
#     def visit_Add(self,node):
#         return self.visit(node.left) + self.visit(node.right)
#
#     def visit_Sub(self,node):
#         return self.visit(node.left) - self.visit(node.right)
#
#     def visit_Mul(self,node):
#         return self.visit(node.left) * self.visit(node.right)
#
#     def visit_Div(self,node):
#         return self.visit(node.left) / self.visit(node.right)
#
#     def visit_Negate(self,node):
#         return -self.visit(node.operand)
#

if __name__ == '__main__':
    import time
    print(sys.getrecursionlimit() )
    start = time.time()
    a = Number(0)
    for n in range(30000000):
        a = Add(a,Number(n))
        e = Evaluator()
    print(e.visit(a))
    print('lapsed time:',time.time()-start)


#     import time
#     start = time.time()
#     t1 = Sub(Number(3),Number(4))
#     t2 = Mul(Number(2),t1)
#     t3 = Div(t2,Number(5))
#     t4 = Add(Number(1),t3)
#
#     e = Evaluator()
#     print(e.visit(t4))
#     print('lapsed time:', time.time() - start)