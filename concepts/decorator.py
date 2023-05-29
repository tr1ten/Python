import time
def timeme(fn):
    def inner(*args):
        start = time.process_time()
        val = fn(*args)
        end = time.process_time()
        print("Execution time {:.2f} ms".format((end-start)*10**6))
        return val
    return inner

@timeme
def pow(a,b):
    return a**b
def fastpow(a,b):
    if(b==1): return a
    p = fastpow(a,b//2)
    if(b&1==0):
        return p*p
    else:
        return p*p*a
def pow(a):
    return pow(2,a)

