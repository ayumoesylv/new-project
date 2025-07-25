import math
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

# EXERCISE 7.1 - UNFINISHED
def mysqrt(a, x):
    epsilon = 0.000000001
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    """
    Prints a table
    Implementation 
        loop through different float values
        log values for float, mysqrt, value from math, and the difference between the two
        use print() params to make table with each of the values

    Challenges
        How to get all the numbers to line up with each other
        Controlling the length of each value (in terms of decimal point)
    """
    print('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff')
    print('-', '---------', '------------', '----')
    for i in range(2):
        num = float(i+1) 
        my_val = mysqrt(i+1, 1)
        mod_val = math.sqrt(i+1)
        diff = abs(my_val - mod_val)
        print(num, my_val, mod_val, diff, sep='\t')


# EXERCISE 7.2 - FINISHED
def eval_loop():
    """
    computs user's math input

    params
    returns
    raises
    """
    while True: 
        request = input('Type in a request:\n')
        if request == 'done':
            print('exiting program!')
            break
        else: 
            result = eval(request)
            print(result)
    return result


# EXERCISE 7.3 - UNFINISHED
def estimate_pi():
    return



# DRIVERS
print_n('hello', 3)
print(mysqrt(4, 1))
test_square_root() #7.1
eval_loop() #7.2
