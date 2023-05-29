from collections import defaultdict
from functools import reduce
# 1
def foo(t,e): return t.index(e)
# print(foo((1,2,3,4), 2))
def unzip(tps):
    return reduce(lambda acc,x:  list(map(lambda  t:acc[t[0]].append(t[1]) ,enumerate(x)))  and acc,tps,[[] for i in range(len(tps[0]))])
def unzip2(tps):
    res = []
    for x in tps:
        for i in range(len(x)):
            if(i>=len(res)): res.append([])
            res[i].append(x[i])
    return res
print(*unzip2( [[1,2,3],[3,4]]) )

def removeEmpty(ls):
    return list(filter(lambda x:x,ls))

# print(removeEmpty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]))
def keyInDict(d,k):
    return k in d
# print(keyInDict({'a': 100, 'b': 200, 'c': 300}, 'b'))
def sqDict(n):
    return dict([(i,i*i) for i in range(1,n+1)])
# print(sqDict(5))
def maxInDict(d):
    return max(d,key=lambda x:d[x])
# print(maxInDict({'x': 500, 'y': 5874, 'z': 560}))
def minInDict(d):
    return min(d,key=lambda x:d[x])
# print(minInDict({'x': 500, 'y': 5874, 'z': 560}))


def success(ls):
    return reduce(lambda acc,x:acc+x['success'],ls,0)
# print(success([{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]))


def mergeDuplicate(ls1,ls2):
    return reduce(lambda acc,x:acc[x[0]].append(x[1]) or acc,zip(ls1,ls2),defaultdict(list))

# print(mergeDuplicate(['Clas-V', 'Class-VI', 'Class-VI', 'Class-VIII'], [1, 2, 2, 3]))