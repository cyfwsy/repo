'''秒表计时器'''
import time
class Timer:
    def __init__(self,func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

# Example
def countdown(n):
    while n > 0:
        n -= 1

# Use1 a explicit start/stop
t = Timer()
t.start()
countdown(10000000)
t.stop()
print('Elapsed time',t.elapsed)
t.reset()

# Use2 As a context manager
with t:
    countdown(10000000)
print('Elapsed time',t.elapsed)

with Timer(time.process_time) as t2:
    countdown(10000000)
print('Elapsed time',t2.elapsed)
