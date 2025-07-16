def sum_all(*args):
    total = 0
    for i in args: 
        total += i
    return total

sum_all(1, 2, 3, 4)