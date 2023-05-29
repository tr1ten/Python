import math
import turtle


# Ques 1
def pentArea():
    r = int(input("Enter the length from the centre of the pentagon to a vertex "))
    s = 2 * r * math.sin(math.pi / 5)
    area = (3 * math.sqrt(3) * (s ** 2)) / 2

    print(area)


# Ques 2
def pentArea2():
    s = int(input("Enter the length of a side of the pentagon"))
    area = (5 * (s ** 2)) / (4 * math.tan(math.pi / 5))

    print(area)


# pentArea2()


# Ques 3
def Reverse():
    n = input("Enter a 4-digit number")
    print(n[::-1])


# Reverse()


# Ques 4

def draw():
    r = int(input("Enter the radius of the circle"))
    t = turtle.Turtle()

    # Draw the first three circles
    for i, color in ([[1, "blue"], [2, "black"], [3, "red"]]):
        t.color(color)
        t.pensize(4)

        t.circle(r)

        t.up()
        t.setx((2 * r * i))
        t.down()

    # Reposition the pen
    t.up()
    t.sety((r * -1))
    t.setx(r)
    t.down()

    # Draw the next two circles
    for i, color in ([[4, "yellow"], [5, "green"]]):
        t.color(color)
        t.pensize(4)

        t.circle(r)

        t.up()
        t.setx(r + (2 * r * (i - 3)))
        t.down()


draw()
