"""Generator of powers of 3"""


def powers_of_three():
    """Generates powers of three from 0 to infinity"""
    first, second = 1, 3
    while 1:
        yield first
        first, second = second, second * 3


# testing code
COUNTER = 0
for n in powers_of_three():
    print(n)
    COUNTER += 1
    if COUNTER == 10:
        break
