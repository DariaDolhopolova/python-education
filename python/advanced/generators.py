"""Generators exercise"""


def fib():
    """Generator that calculates and outputs the numbers from Fibonacci sequence"""
    first, second = 1, 1
    while 1:
        yield first
        first, second = second, first + second

#import types

# testing code
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")
#     counter = 0
#     for n in fib():
#         print(n)
#         counter += 1
#         if counter == 10:
#             break
