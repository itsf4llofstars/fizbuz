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
    """Computes the product of two numbers and returns
    the product

    Args:
        num_one (int): One of the numbers to be multiplied
        num_two (int): The second number to be multiplied

    Return:
        product_numbers (int): The product of the two numbers
    """
    product_numbers: int = num_one * num_two
    return product_numbers


def divide(num_one: int, num_two: int) -> int:
    """Divides two numbers and return their quotiant

    Args:
        num_one (int): The numerator
        num_two (int): The denomenator
    
    Return:
        answer (int): num_one divided by num_two
    """
    try:
        answer: int = num_one / num_two
    except ZeroDivisionError as zde:
        print(f"{zde}")
    else:
        return answer


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
