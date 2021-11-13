"""This module implements factorial function using recursion."""


def recursive_factorial(num):
    """Function returns the current number and the call of itself with number - 1,
    so it calculates factorial recursively."""
    if num <= 1:
        return 1
    return num * recursive_factorial(num - 1)


if __name__ == "__main__":
    print(recursive_factorial(3))
    print(recursive_factorial(0))
