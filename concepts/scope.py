def foo():
    res = 0
    def boo():
        nonlocal res
        res = 1
    boo()   
    print(res)
foo()

a = 10
def foo():
    a = 1
    return a+1
print(foo(),a)
ls = [1,2]
ds = ls.copy()
ds[0] = 9
print(ls,ds)