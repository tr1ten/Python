from turtle import *
pen = Pen()
def draw_polygon(side,n):
    theta = (n-2)*180/n;
    for x in range(n):
        pen.right((180-theta))
        pen.fd(side)
    mainloop()

if __name__=="__main__":
    draw_polygon(100,4)
