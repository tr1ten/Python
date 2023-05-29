import time
from decorator import timeme
class EvenIter:
    def __init__(self,mx) -> None:
        self.mx = mx
        self.cur = 0
    def __iter__(self):return self
    def __next__(self):
        if(self.cur+2<=self.mx):
            self.cur +=2
            return self.cur
        else:
            raise StopIteration
def even_gen(mx):
    cur = 0
    while(cur<=mx):
        yield cur
        cur +=2
        print("gen waiting...")
        time.sleep(1)
@timeme
def foo():
    e2 = even_gen(6)
    for x in e2:
        print(x)
        print('foo waiting..')
        time.sleep(1)
huh = EvenIter(2)
print(huh)
# for x in huh:
#     print(x)


# a generator is a kind of iterator
# iterator is a more general concept: any object 
# whose class has a __next__ method (next in Python 2) and an __iter__ method that does return self.
# Iterables are any objects you can get an iterator from.