def solveQuadratic():
    a,b,c = map(int, input().split())
    d = b**2 - 4*a*c
    if d < 0:
        print("No real roots")
    elif d == 0:
        print("One real root")
        print(-b/(2*a))
    else:
        print("Two real roots")
        print((-b + d**0.5)/(2*a))
        print((-b - d**0.5)/(2*a))
# solveQuadratic()
def crammer():
    a,b,c,d,e,f = map(int, input().split())
    if(a*d - b*c == 0):
        print("No solution")
        return;
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print(x,y)
# crammer()
import random
def quiz():
    a,b = random.randint(1,100), random.randint(1,100)
    print("Sum of nums ?",a,b)
    ans = int(input())
    print(ans==a+b)

# quiz()
# Write a program that prompts the user to enter an integer for today's day of the week
# (Sunday is 0, Monday is 1…, and Saturday is 6). Also prompt the user to enter the
# number of days after today for a future day and display the future day of the week.
def day():
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    today = int(input())
    future = int(input())
    print(days[(today+future)%7])

# day();
# Suppose you shop for rice and find it i two different sized packets. You would like to
# write a program to compare the costs of the packages. The program prompts the user to
# enter the weight and price of each package and the displays the one with the better price.
def rice():
    w1,p1 = map(int, input().split())
    w2,p2 = map(int, input().split())
    if(p1/w1 < p2/w2): print("Package 1 is better")
    elif(p1/w1 > p2/w2): print("Package 2 is better")
    else: print("Same price")
# rice();
#(Find the number of days in a month) Write a program that prompts the user to enter the
# month and year and displays the number of days in the month. For example, if the user
# entered month 2 and year 2000, the program should display that February 2000 has 29
# days. If the user entered 3 and year 2005, the program should display that March 2005
# has 31 days.
def days():
    m,y = map(int, input().split())
    if(m==2):
        if(y%4==0 and y%100!=0 or y%400==0): print("29 days")
        else: print("28 days")
    elif(m==4 or m==6 or m==9 or m==11): print("30 days")
    else: print("31 days")

# days();
# Write a program that prompts the user to enter an integer and check whether the number
# is divisible by both 5 and 6, divisible by 5 or 6 or just one of them (but not both of them).
def divby():
    n = int(input())
    if(n%5==0 and n%6==0): print("Div by both")
    elif(n%5==0 or n%6==0): print("Div by one")
    else: print("Not div by either")

# divby();
# Write a program that reads three edges for a triangle and computes the perimeter if the
# input is valid. Otherwise, display that the input is invalid. The input is valid if the sum of
# every pair of two edges is greater than the remaining edge.
def triangle():
    a,b,c = map(int, input().split())
    if(a+b>c and a+c>b and b+c>a): print(a+b+c)
    else: print("Invalid")
    
# triangle()
# Write a program that prompts the user to enter a hex character and displays its
# corresponding decimal integer.

def hex2dec():
    n = input()
    print(int(n,16))
    
hex2dec()

