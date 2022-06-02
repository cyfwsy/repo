'''测试 堆优先队列'''
import heapq
import random

class heapQ:
    def __init__(self,init_elem = None):
        self.init_elem = init_elem
        if self.init_elem != None:
            self._array = list(init_elem)
            heapq.heapify(self._array)
        else:
            self._array = []

    def heap_add(self,elem):
        heapq.heappush(self._array,elem)

    def priority_get(self): # get a priority element
        return heapq.heappop(self._array)

    def heap_show(self):
        print(self._array)

# p_q = heapQ((2,7,9,23,45,99,34,28,37,1))
# p_q.heap_add((19))
# p_q.heap_add((78))
# p_q.heap_show()
# print(p_q.priority_get())
p_q = heapQ()
for i in range(10):
    p_q.heap_add(random.randint(1,200))
print(p_q.heap_show())
print(p_q.priority_get())
print(p_q.priority_get())
print(p_q.priority_get())
print(p_q.heap_show())


