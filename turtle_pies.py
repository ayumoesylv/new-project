import turtle 
import math
bob = turtle.Turtle()

def deg_to_rad(deg): 
    angle = deg * (math.pi / 180)
    return angle

def pie(t, n, l):
    """
    Draws a turtle pie 

    params:
    t = turtle object
    n = number of slices
    l = length of each slice side
    """
    beta = 360 / n # the inner angle of each slice
    alpha = (180 - beta) / 2
    beta_rad = deg_to_rad(beta)
    alpha_rad = deg_to_rad(alpha)
    start_angle = beta / 2
    pivot_angle = 90 + (180 / n)
    numer = math.sin(beta_rad)
    denom = math.sin(alpha_rad)
    s = (numer / denom) * l

    t.lt(start_angle)
    for i in range(n): 
        t.fd(l)
        t.lt(pivot_angle)
        t.fd(s)
        t.lt(pivot_angle)
        t.fd(l)
        t.lt(180)

pie(bob, 7, 100)