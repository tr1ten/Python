from turtle import *

r = 100
colors = ['blue','black','red','yellow','green']
width(20)
speed(10)
penup()
back(100)
for i in range(5):
    color(colors[i])
    pendown()
    circle(r)
    penup()
    forward(2.5*r)
    if(i==2):
        goto((0.4*r,-0.8*r))