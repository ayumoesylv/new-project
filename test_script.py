def print_element(f, v1, v2):
    f(v1, v2, v2, v2, v2, end=' ')

def do_twice(f, g, v1, v2):
    f(g, v1, v2)
    f(g, v1, v2)

def do_four(f, v1, v2):
    f(v1, v2)
    f(v1, v2)
    f(v1, v2)
    f(v1, v2)
    return

def add_row(v1, v2):
    do_twice(print_element, print, v1, v2)
    do_twice(print_element, print, v1, v2)
    print(v1)

def make_grid():
    add_row('+', '-')
    do_four(add_row, '|', ' ')
    add_row('+', '-')
    do_four(add_row, '|', ' ')
    add_row('+', '-')
    do_four(add_row, '|', ' ')
    add_row('+', '-')
    do_four(add_row, '|', ' ')
    add_row('+', '-')

make_grid()

