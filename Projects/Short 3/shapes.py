def shape_alpha():
    return [[10, 'abc', 'jkl', 40], [[1.1, -17], [123, 456]]]

def shape_bravo():
    beta = ['bogus', 'righteous']

    return [[['whoa', 'excellent'], beta], [beta, 'rufus']]

def shape_charlie(arg1):
    arr = [None, arg1]
    for _ in range(3):
        arr[0] = arr
    return arr

def shape_delta(arg1, arg2):
    return [arg1, arg2, [arg1, [arg1, arg2, [arg1, arg2], [30]], [20], arg2], [10]]

def shape_echo(arg1, arg2, arg3):
    arr = [[[None, arg3], arg2], arg1]
    arr[0][0][0] = arr
    return arr
