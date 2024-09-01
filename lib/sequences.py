#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Start the list with the first two Fibonacci numbers
    fibonacci_list = [0, 1]

    # Generate the Fibonacci sequence until it reaches the desired length
    while len(fibonacci_list) < length:
        # Add the sum of the last two elements to the list
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    print(fibonacci_list)
