from turtle import Turtle
from math import sin,cos,radians
def exp1():
    point1 = (0,0)
    point2 = (100,100)
    mid_pt = ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)
    def euclidean_distance(point1,point2):
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
    print(euclidean_distance(point1,point2),mid_pt)
# exp1()
# Write a program to represent the five circles having different radius and same center.
def exp2():
    t = Turtle()
    for i in range(50):
        t.penup()
        t.goto(0,-10*(i+1))
        t.pendown()
        t.circle(10*(i+1))
# exp2()

# Write a program to a pentagon and put a line from each vertex to the center. Fill different
# color in each block.
def exp3():
    t = Turtle()
    t.speed(1)
    S = 300 # side length
    sn = 3
    inner=360/sn
    a = S/(2*sin(radians(inner/2))) # side length of the triangle isosceles
    def trig():
        t.right(inner/2)
        t.forward(a)
        t.left((180+inner)/2)
        t.forward(S)
        t.left((180+inner)/2)
        t.forward(a)
        t.right(180+inner/2)
    for i in range(sn):
        # t.right(inner);
        t.fillcolor((i/sn,i/sn,i/sn))
        t.begin_fill()
        trig()
        t.end_fill()
    input()
exp3()
# Write a program to read a gray image and convert it to the binary image. Write both the
# image.
def exp4():
    import cv2
    img = cv2.imread('images/lena_gray.png',0)
    cv2.destroyAllWindows()
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow('binary',thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# exp4()
# Write a program to read a color image and extract its pixel value in the red, green and
# blue dimension.
def exp5():
    import cv2
    img = cv2.imread('images/lena_color.jpeg')
# exp5();