import turtle,time
wn = turtle.Screen()
wn.setup(width = 600,height = 600)
wn.title("Analog clock")
wn.bgcolor("black")
wn.tracer(0) # this is to turn off the animation
pen = turtle.Turtle() 
pen.hideturtle() # this is to hide the pen
pen.width(3)
R,H_L,M_L,S_L,C = 210,100,150,180,"white" # Constants (Radius, Hour Line, Minute Line, Second Line, Color)
pen.color(C)
def loop():
    pen.up() # draw clock face
    pen.goto(0,R)
    pen.setheading(180)
    pen.pendown()
    pen.circle(R)
    for i in range(12,0,-1): # draw the hour lines
        pen.up() 
        pen.goto(0,0)
        pen.setheading(90)
        pen.rt(30*i) # rotate the pen by 30*i degrees
        pen.fd(R-10)
        pen.down()
        pen.write(i,align="center",font=("Verdana", 23, "normal"))
        pen.fd(10)
    h,m,s = time.localtime()[3:6] # get the current time
    for i,j,k in zip([h,m,s],[H_L,M_L,S_L],[360,360/5,360/5]):
        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)
        pen.right((i/12)*k)
        pen.down()
        pen.fd(j)
while True:
    loop()
    wn.update() # refresh the screen
    time.sleep(1) # wait for 1 second
    pen.clear() # clear the screen
