import time
class cm_timer_1:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(elapsed)

with cm_timer_1() as timer: # as передаёт значение из return в timer в данном случае
    time.sleep(2)
    
# print(timer.start)

from contextlib import contextmanager

@contextmanager
def context_manager2():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
