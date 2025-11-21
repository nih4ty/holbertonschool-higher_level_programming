#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

from add_0 import add

a = 1
b = 2

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
