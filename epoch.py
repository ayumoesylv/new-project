import time
import turtle
epoch = time.time()
bob = turtle.Turtle()

hrs = epoch // 3600
mins = (epoch // 60) - (hrs * 60)
secs = epoch - (mins * 60)

print(hrs, mins, secs)

def check_fermat(a, b, c, n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    rh = (a**n) + (b**n)
    if (rh == c):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

#a = input('input a number a:\n')
#b = input('input a number b:\n')
#c = input('input a number c:\n')
#n = input('input a power n:\n')
# check_fermat(a, b, c, n)


def is_triangle(a, b, c):
    """
    determines if three integer lengths can form a triangle

    a, b, c are various lengths of triangle
    """
    if (a+b >= c) or (b+c >= a) or (a+c >= b):
        print('no')
    else:
        print('yes')

def test_your_tri():
    a = int(input('input 1st side length:\n'))
    b = int(input('input 2nd side length:\n'))
    c = int(input('input 3rd side length:\n'))
    is_triangle(a, b, c)


# test_your_tri()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

#draw(bob, 10, 3)

def compare(x, y):
    if x > y: 
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print(compare(4, 3))

