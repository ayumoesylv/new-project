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

polygon(bob, 100, 5)