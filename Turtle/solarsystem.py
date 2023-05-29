from turtle import Turtle
from math import sin, cos, radians

sun = Turtle()
sun.shape('circle')
sun.color('yellow') 
sun.dot(100)
N = 4
planets = [[Turtle(shape="circle"),d,0] for d in range(1,N+1)]
while 1:
  for x in planets:
    x[0].penup();
    x[0].setpos((x[1]*80*cos(x[2]),x[1]*80*sin(x[2])))
    x[2] += radians(1+ (N-x[1])/2)
