def annoying_factorial(n):
    # makes sure we have a valid input as outlined by the project spec
    assert type(n) is int and n >= 0, f'invalid input: {n}'
    # the non-hardcoded recursion is just multiplying the current value by 
    # the factorial of the one below it
    if n > 6:
        return n * annoying_factorial(n-1)
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 4 * annoying_factorial(3)
    if n == 5:
        return 5 * annoying_factorial(4)
    if n == 6:
        return 6 * annoying_factorial(5)

def annoying_fibonacci(n):
    # makes sure we have a valid input as outlined by the project spec
    assert type(n) is int and n >= 0, f'invalid input: {n}'
    # every fibanacci number is given by the sum of the previous two fibanacci 
    # numbers
    if n > 6:
        return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)
    # fibanacci numbers 1 and 2 must always be hardcoded as 0 and 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    if n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    if n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
