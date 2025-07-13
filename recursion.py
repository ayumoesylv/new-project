def countdown(n):
    if n <= 0: 
        print('Blastoff!')
    else: 
        print(n)
        countdown(n-1)
    
countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    else:
        print(s)
        print_n(s, n-1)

print_n('hello', 3)

def test(s):
    print(s)

def do_n(f, n): 
    if n <= 0:
        return
    else: 
        f(n-1)

do_n(test, 3)