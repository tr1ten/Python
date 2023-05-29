from turtle import *
from math import pi,radians,cos,sin
a,b,alpha,theta = 100,50,pi/2,0
def coors(theta): 
    return (a*cos(theta)*cos(alpha) - b*sin(theta)*sin(alpha),a*cos(theta)*sin(alpha) + b*sin(theta)*cos(alpha))
penup()
goto(coors(theta))
pendown()
while theta < 2*pi:
    goto(coors(theta))
    theta += radians(1)