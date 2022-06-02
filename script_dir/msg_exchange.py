'''消息交换中介'''
from contextlib import contextmanager
from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self,task):
        self._subscribers.add(task)

    def detach(self,task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self,*tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self,msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

# Dictionary of all created exchange
_exchange = defaultdict(Exchange)
def get_exchange(name):
    return _exchange[name]

class DisplayMessage:
    def __init__(self):
        self.count = 0

    def send(self,msg):
        self.count += 1
        print('msg[{}]:{!r}'.format(self.count,msg))

exch1 = Exchange()
exch2 = Exchange()

_exchange['A_center'] = exch1
_exchange['B_center'] = exch2

task_currents = (DisplayMessage() for i in range(10))
# task_a = DisplayMessage()
# task_b = DisplayMessage()

exc = get_exchange('A_center')
with exc.subscribe(*task_currents):
    exc.send('hello, Andi')
    exc.send('hello 老王')