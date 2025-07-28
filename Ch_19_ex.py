import math
"""
Exercises to finish
    Page 187 - rewrite avoids using sets
    Page 189 - rewrite using default dict
    End of chapter 1 exercise
"""

# PAGE 184 DEMO CODE
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# PAGE 184 DEMO CODE
def capitalize_all(t):
    return [s.capitalize() for s in t]

# PAGE 185 DEMO CODE
def only_upper(t):
    return [s for s in t if s.isupper()]

y = math.log(x)