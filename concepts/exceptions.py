# finally execute even if there is return or raise statement in try or catch block

class NegativeNumber(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
def sqrt(x):
    if x<0: raise NegativeNumber("Negative number not allowed")
    return x**0.5
# def me(b=False):
#     try:
#         if b: return "BOO"
#         Exception("NO")
#     except:
#         raise Exception("YES")
#     finally:
#         print("finally")
#     print("putside")
# me(True)

if __name__=="__main__":
    try:
        print(sqrt(-1))
    except NegativeNumber as e:
        print(e)
    finally:
        print("finally")
    print("putside")
        