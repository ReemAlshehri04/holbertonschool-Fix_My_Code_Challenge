#!/usr/bin/python3
""" FizzBuzz """
import sys


def fizzbuzz(n):
    """
    Prints the numbers from 1 to n separated by a space.

    For multiples of 3 print "Fizz".
    For multiples of 5 print "Buzz".
    For multiples of both 3 and 5 print "FizzBuzz".
    """
    if n < 1:
        return

    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    print(" ".join(result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)