def miltok():
    print("Miles\t\t Kilometers")
    for i in range(1,11):
        print(i,"\t\t",i*1.609)
# miltok() 
def tuition():
    t = 10000
    sm = 10000
    for i in range(10):
        t += t*0.05
        sm += t
        if(i<3): print(t)
    print("tution fees in 10 years: ",t)
    print("total cost of 4 years: ",sm)
# tuition()
def pprint():
    cnt = 0
    for i in range(100,1001):
        if(i%5==0 and i%6==0):
            print(i,end=" ")
            cnt +=1
            if(cnt==10):
                print()
                cnt = 0
# pprint()        
def ppascii():
    i = 0;
    start = ord('!')
    end = ord('~')
    cnt = 0
    while(start+i<end):
        print(chr(start+i),end=" ")
        cnt +=1
        if(cnt==10):
            print()
            cnt = 0
        i +=1
# ppascii()
# patterns 
def pattern_A():
    n  =  int(input("Enter the number of rows : "))
    for i in range(1 ,n+1):
        print("")
        for j in range(1 ,n+1):
            if(j<=i):
                print(j ,end=" ")
            else:
                print(" " ,end=" ")
def pattern_B():
    n  =  int(input("Enter the number of rows : "))
    for i in range(n ,0,-1):
        print("")
        for j in range(1 ,n+1):
            if(j<=i):
                print(j ,end=" ")
            else:
                print(" " ,end=" ")
def pattern_C():
    n  =  int(input("Enter the number of rows : "))
    for i in range(1 ,n+1):
        print("")
        for j in range(n ,0,-1):
            if(j<=i):
                print(j ,end=" ")
            else:
                print(" " ,end=" ")
def pattern_D():
    n  =  int(input("Enter the number of rows : "))
    for i in range(n ,0,-1):
        print("")
        for j in range(1 ,n+1):
            if(j<=i):
                print(j ,end=" ")
            else:
                print(" " ,end=" ")
pattern_A()
pattern_B()
pattern_C()
pattern_D()

def pat():
    n = int(input())
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(i):
            print(2**j,end="")
        for j in range(i-2,-1,-1):
            print(2**j,end="")
        print()
# pat()  
#  Ques 11

def combinations():
    list = [1, 2, 3, 4, 5, 6, 7]
    cnt = 0
    for i in range(0, 7):
        for j in range(i + 1, 7):
            print(list[i], end="  ")
            print(list[j])
            cnt += 1

    print("Total combinations = ", cnt)


# combinations()

# Ques 10

def perfection():
    for i in range(6, 10000):
        curr = i
        s = 0

        for j in range(1, curr // 2 + 1):
            if i % j == 0:
                s += j

        if curr == s:
            print("Perfect number: ", curr)


# perfection()

# QUES 8

def Minterest():
    amt = int(input("Enter the loan amount"))
    lp = int(input("Enter the loan period"))
    for i in range(40, 64):
        interest = i / 8
        ttl_pay = amt + (amt * lp * interest / 100)
        print(f"Total payment at {interest} % is {ttl_pay}\
     and monthly payment is {ttl_pay / (lp * 12)}")


# Minterest()