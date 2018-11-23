
from time import time
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('Tiempo transcurrido:', after-before)
        return rv
    return f

@timer
def add(x, y=10):
    return x + y

@timer
def sub(x, y=10):
    return x - y

print('add(10)', add(10))
print('add(10,20)', add(10,20))
print('sub(10,20)', sub(10,20))
