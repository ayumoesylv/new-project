import math

# PAGE 65 DEMO CODE
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1


# PAGE 66 EXERCISE - FINISHED; UNCHECKED
def print_n(s, n): 
    while n > 0:
        print(s)
        n -= 1


# EXERCISE 7.1 - FINISHED; UNCHECKED
def mysqrt(a, x):
    """
    Returns an estimate of the square root of a given initial guess x
    
    params
        a (int) = integer to find square root of
        x (int) = initial estimate
    returns
        x (int) = estimated square root of a
    raises
        None
    """
    epsilon = 0.000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def add_padding(s, c):
    """
    returns a string with padding to fill the character length of a column
    params
        s (str) = string in column 
        c (int) = character length of column 
    returns
        s (str) = string with right padding
    raises
        None
    """
    pad_length = c - len(s)
    s = s + (' ' * pad_length)
    return s

def test_square_root():
    """
    Prints a table to test differences of mysqrt() and math.sqrt()

    params
        None
    returns
        None
    raises
        None
    """
    print(add_padding('a', 4), add_padding('mysqrt(a)', 19), add_padding('math.sqrt(a)', 19), 'diff', sep='')
    print(add_padding('-', 4), add_padding('---------', 19), add_padding('------------', 19), '----', sep='')
    for i in range(9): # i -> [0, 1]
        num = float(i+1) 
        my_val = float(mysqrt(i+1, 1))
        mod_val = math.sqrt(i+1)
        diff = abs(my_val - mod_val)

        num = add_padding(str(num), 4)
        my_val = add_padding(str(my_val), 19)
        mod_val = add_padding(str(mod_val), 19)
        

        print(num, my_val, mod_val, diff, sep='')


# EXERCISE 7.2 - FINISHED; UNCHECKED
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


# EXERCISE 7.3 - FINISHED; UNCHECKED
def estimate_pi():
    """
    Returns an estimate of the value of 1/pi

    params
        None
    returns
        estim (float): estimate of 1/pi
    raises
        None
    """
    summ = 0.0
    epsy = 1e-15
    k = 0
    
    while True:
        numerator = math.factorial(4 * k) * ( 1103 + (26390 * k) )
        denominator = (math.factorial(k) ** 4) * (396 ** (4 * k) )
        term = numerator / denominator
        if abs(term) < epsy: 
            break
        summ += term
        k += 1
    
    estim = summ * ((2 * math.sqrt(2)) / 9801)
    print(estim, 1/math.pi, abs(estim - 1/math.pi))
    return estim



# EXECUTES

# countdown(10) # Page 65 demo code
# sequence(10)

# print_n('hello', 3) # Page 66 ex 1

# print(mysqrt(4, 1)) # Eoc ex 7.1
# test_square_root() 

# eval_loop() # Eoc ex 7.2

# estimate_pi() # Eoc ex 7.3