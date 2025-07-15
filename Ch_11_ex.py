def histogram(s):
    d = dict()
    for i in s: 
        value = d.get(i, 0)
        d[i] = value + 1
    print(d)
    return d

def invert_dict(d):
    inverse = dict()
    for i in d:
        value = d[i]
        if value not in inverse:
            inverse[value] = [i]
        else:
            inverse[value].append(i)
    print(inverse)
    return inverse


hist = histogram('hello')
invert_dict(hist)