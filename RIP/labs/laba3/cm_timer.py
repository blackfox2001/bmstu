import time
from contextlib import contextmanager


class cm_timer_2:

    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- %s seconds ---" % (time.time() - self.start_time))


@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    print("--- %s seconds ---" % (time.time() - start_time))