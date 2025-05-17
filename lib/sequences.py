#!/usr/bin/env python3

def print_fibonacci(length):
    """Prints a list of Fibonacci numbers of the given length."""
    if length <= 0:
        print([])
        return
    fib = [0, 1]
    if length == 1:
        print([0])
        return
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    print(fib[:length])
