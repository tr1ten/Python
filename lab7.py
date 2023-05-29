def ismepty(ls):
    print(all([not d for d in ls]))

# ismepty([{},{},{}])
# ismepty([{1,2},{},{}])

def mint(ls):
    print(min(ls,key=lambda x:x[1]))
    
mint([(1,2,3),(4,5,6)])

def listToDict(ls,keys):
    print(list(map(lambda x:dict(list(zip(keys,x))),zip(*ls))))
# listToDict([["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]],["color_name","color_code"])

from functools import reduce
def flatten(ls):
    print(sorted(set(reduce(lambda acc,x:acc+x,ls,list()))))
    
# flatten([[1,2],[3,1]])

def identical(x1,x2):
    print(("".join(map(str,x1+x1))).count("".join(map(str,x2)))>0)
    
# identical([1,2,3,4],[4,1,2,3])
# identical([1,2,3,4],[4,1,2,2])
def common(x1,x2):
    print(len(set(x1)&set(x2))!=0)

# common([1,2],[3,1])

def sq5():
    print(list(map(lambda x:x*x,list(range(1,5))+list(range(26,31)) )))

# sq5()

def foo(ls):
    print([len(s)>1 and s[0]==s[-1] for s in ls].count(1))

# foo(['abc', 'xyz', 'aba', '1221'])

def mul(ls):
    print(reduce(lambda acc,x:acc*x,ls))
# mul([1,2,3,4])