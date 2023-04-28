#!/usr/bin/env python
import os
import sys


def add_numbers(num_one: int, num_two: int) -> int:
    """Adds two passed number and returns their sum

    Args:
        num_one (int): One of the numbers to be added
        num_two (int): The second number to be added

    Return:
        added_numbers (int): The sum of the two numbers
    """
    added_numbers: int = num_one + num_two
    return added_numbers


def product(num_one: int, num_two: int) -> int:
    """doc
    """
    pass


def main():
    num1: int = 23
    num2: int = 71

    added: int = add_numbers(num1, num2)

    print(f"{num1} + {num2} = {added}")

    product_nums: int = product(num1, num2)
    print(f"{num1} * {num2} = {product_nums}")


if __name__ == "__main__":
    os.system("clear")

    sys.exit(main())
