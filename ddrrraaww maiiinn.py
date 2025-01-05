from turtle import *
import math
from math import *


def turtle():
    bgcolor("black")
    turtlesize(2, 3, 0)  # width,length,outline thickness
    color("red")  # drawing and outline
    fillcolor("darkslategray3")  # inside turtle
    #  shape('circle')

    speed(1000)
    pensize(2)
    screensize(5000, 3000)


def jump(length):
    penup()
    forward(length)
    pendown()


def triangle(lengtha, anglea):
    global angleb
    angleb = 180 - anglea * 2
    global lengthbb
    lengthbb = sqrt(
        ((lengtha**2) + (lengtha**2)) - (2 * lengtha * lengtha * cos(radians(angleb)))
    )
    forward(lengthbb)
    left(180 - anglea)
    forward(lengtha)
    left(180 - angleb)
    forward(lengtha)
    left(180 - anglea)


def drawpie(length, number):
    angle_to_number_of_triangle = 360 / number
    interior_angle = 180 - angle_to_number_of_triangle
    for i in range(number):
        triangle(length, interior_angle)
        jump(lengthbb)
        left(angle_to_number_of_triangle)


def drawshuriken(length):  # write length 80 because of the circle
    number_of_triangle = 4  # (minimmum)
    angle_to_number_of_triangle = 360 / number_of_triangle
    for i in range(number_of_triangle):
        triangle(length, 180 - angle_to_number_of_triangle / 2)
        left(angle_to_number_of_triangle)
    penup()
    goto(lengthbb, lengthbb - 15)
    pendown()
    circle(20)
def heart_shape1(l):
    x=16*sin(l)**3
    y=13*cos(l)-5*cos(2*l)-2*cos(3*l)-cos(4*l)
    return x,y
def heart_draw():
    penup()
    for t in range (10):
        goto(0,0)
        for i in range(0,100,2):
            pendown()
            x,y=heart_shape1(i/10)
            goto(x*t,y*t)
        penup()
            # goto(heart_shape1(i/10)*t,heart_shape2(i/10)*t)
# # test


# def polyline2(n, length, jumpp, angle):
#     for i in range(n):
#         forward(length)
#         left(angle)
#         jump(jumpp)
#         left(angle)


# def polyline3(n, length, jumpp, angle):
#     for i in range(n):
#         jump(jumpp)
#         left(angle)
#         forward(length)
#         left(angle)


# def rectangle2(tall, wide):
#     polyline2(2, wide, tall, 90)
#     polyline3(2, tall, wide, 90)


def parallelogram(length1, length2, angle):
    Eangle = 180 - angle
    polyline(1, length1, angle)
    polyline(1, length2, Eangle)
    polyline(1, length1, angle)
    polyline(1, length2, Eangle)


def polyline(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)


def polygon(length, n):
    angle = 360 / n
    polyline(n, length, angle)


def arc(r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = 150
    segment_length = arc_length / n
    segment_angle = angle / n  # modify
    polyline(n, segment_length, segment_angle)


def circle(r):
    # circumference = 2 * math.pi * r
    # n=150
    # segment_length=circumference/n
    # segment_angle=360/n
    # polyline(n,segment_length,segment_angle)# this all can be replaced with arc like this

    arc(r, 360)


def petal():
    arc(50, 120)
    left(60)
    arc(50, 120)
    left(60)


def flower():
    for i in range(6):
        petal()
        right(60)


def rhombus(length, angle):
    parallelogram(length, length, angle)


def rectangle(wide, tall):
    parallelogram(wide, tall, 90)


turtle()
# flower()
heart_draw()
# drawshuriken()
hideturtle()
done()
