# def print_n(s, n):
#     if n <= 0:
#         return
#     else:
#         print(s)
#         print_n(s, n-1)


def print_n(s, n): 
    while n > 0:
        print(s)
        n -= 1

    return

print_n('hello', 3)

def square_root(a, x):
    epsilon = 0.000000001
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

print(square_root(4, 2.16))