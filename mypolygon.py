import turtle 
import math
bob = turtle.Turtle()
    
def polyline(t, length, n, angle):
    """
    loops forward movement and left turn 

    t = turtle object
    length = step length
    n = number of steps
    angle = step angle
    """
    for i in range(n): 
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    angle = 360/n
    polyline(t, length, n, angle)


def circle(t, r):
    circumf = 2*r*math.pi
    length = circumf / 1000
    polygon(t, length, 1000)

def arc(angle, t, r):
    """
    draws an arc based on radius of circle 

    angle = angle of arc
    t = turtle object
    r = radius of circle
    """
    n = 50
    arc_length = 2 * r * math.pi * (angle / 360)
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, step_length, n, step_angle)


    # n = 50
    # circumf = 2 * r * math.pi
    # length = circumf / n
    # m = n * (angle/360)
    # for i in range(int(m)):
    #     t.fd(length)
    #     t.lt(360/n)

def flower(t, r, arc_angle, petal_ang):
    """
    t = turtle object
    r = radius 
    arc_angle = angle of each arc
    petal_ang = angle turned after petal
    p = net angle travelled after 1 petal
    """
    additional = petal_ang - 180
    p = 360 / (arc_angle + additional)

    for i in range(int(p)):
        arc(arc_angle, t, r)
        t.lt(180 - arc_angle)
        arc(arc_angle, t, r)
        t.lt(petal_ang)



#flower(bob, 50, 90, 140)

turtle.mainloop()
