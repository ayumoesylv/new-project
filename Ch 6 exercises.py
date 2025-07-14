'''
' PLease write the module desciption
' Author
' Date
'''
import math
'''
PLeae write the description of function,
input paramets
output:
'''

def sample_func_doc(p1, p2):
    """
    Sample description for a function

    Args:
        p1 (float): the first parameter.
        p2 (string): the 2nd parameter.

    Returns:
        float: the return of function.

    Raises:
        ValueError: if p1 is string
    """

    r = p1 + float(p2) # we add two inputs 

    return r # we return the addtion result

def hypotenuse(leg1, leg2):
    leg1 **= 2
    leg2 **= 2
    length = math.sqrt(leg1 + leg2)
    return length

hypotenuse = hypotenuse(3, 4)
print(hypotenuse)

def is_between(x, y, z):
    return x < y < z

result = is_between(2, 3, 4)
print(result)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else: 
#         past_term = factorial(n-1)
#         result = n * past_term
#         return result

# print(factorial(3))

def factorial_debug(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)

    if n == 0 or n == 1:
        print(space, 'returning 1')
        return 1
    
    else: 
        past_term = factorial_debug(n-1)
        result = n * past_term
        print(space, 'returning', result)
        return result
    
print(factorial_debug(3))

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result
    
#factorial(3)