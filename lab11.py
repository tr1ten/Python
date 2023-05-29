class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        d2 = list(d.keys())
        res =0
        for i,x in enumerate(s):
            j = d2.index(x)
            if(j+1<len(d2) and i+1<len(s) and d2[j+1]==s[i+1]): res += -d[x]
            elif(j+2<len(d2) and i+1<len(s) and d2[j+2]==s[i+1]): res += -d[x]
            else: res += d[x]
        return res
# print(Solution().romanToInt("IV"))
class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        st =[]
        mat = {
            "}":"{",
            ")":"(",
            "]":"[",
        }
        for x in s:
            if(x in ['(','{','[']): st.append(x)
            elif(st and st[-1]==mat[x]): st.pop()
            else: return False
        return len(st)==0    

print(Solution.isValid("(())"))
    
# Write a Python class which has two methods get_String and print_String. get_String
# accept a string from the user and print_String print the string in upper case.

class Exp:
    def get_String():
        Exp.s = input()
    def print_String():
        print(Exp.s.upper())
# Exp.get_String()
# Exp.print_String()

# Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r
    
c = Circle(5)
print(c.area())
# Design a class named triangle that extends the GeometricObject class. The Tringle class
# contains:
# 
# 
# 
# 
# 
# Three float fields named side1, side2, and side3 to denote the three sides of the
# triangle.
# A constructor that creates a tringle with the specified side1, side2, and side3, with
# default value 1.0.
# The accessor methods for all three data fields.
# A method named getArea() that returns the perimeter of this triangle.
# A method named _ _ str_ _ () that returns a string description for the triangle.

class GeometricObject:
    pass
class Triangle(GeometricObject):
    def __init__(self,side1=1.0,side2=1.0,side3=1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getArea(self):
        s = (self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def __str__(self):
        return f"Triangle: side1 = {self.side1} side2 = {self.side2} side3 = {self.side3}"
    
    def side1(self):
        return self.side1
    def side2(self):
        return self.side2
    def side3(self):
        return self.side3
    
    
    