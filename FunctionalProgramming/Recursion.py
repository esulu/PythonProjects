# Python recursion test program


def factorial(x):
    if x < 0:
        raise ValueError('Unable to perform calculation')
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(25))
