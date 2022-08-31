import random
import multiprocessing
import time


class ActivePool:

    def __init__(self,shared_list) -> None:
        # super(ActivePool, self).__init__()
        # self.msg = multiprocessing.Manager()
        # self.active = self.msg.list()
        self.active = shared_list
        self.lock = multiprocessing.Lock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.make_active(name)
        print('Activating {} now running {}'.format(name, pool))
        time.sleep(random.random())
        pool.make_inactive(name)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_list = manager.list()
    pool = ActivePool(shared_list)
    s = multiprocessing.Semaphore(3)
    jobs = [
        multiprocessing.Process(
            target=worker,
            name='worker[{}]'.format(i),
            args=(s, pool)
        )
        for i in range(10)
    ]

    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(0.1)
                print('Now running {}'.format(pool))
        if alive == 0:
            # All done
            break
