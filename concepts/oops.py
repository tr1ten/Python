
class A:
    def __init__(self) -> None:
        pass
    def f(a): return a+2;

class B(A):
    def __init__(self) -> None:
        pass
    @staticmethod
    def f(a): return a+10;
def over1(a,b=None):
    if not b: return a+1
    return a+2
print(over1(10,1))
    
    
    