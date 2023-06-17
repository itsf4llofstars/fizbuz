"""fizzbuzz.py"""


def increase_number(number: int, value: int = 1) -> int:
    """Increase the value of a passed number.

    Args:
        number (int): The number to be increased
        value (int): The amount to increas the number defaulte: 1

    Returns:
        (int): The number increased by the value
    """
    return number + value


def mod_five(number) -> bool:
    """Returns a boolean that is oposite of the
    passed number module with 5.

    Args:
        number (int): The number to be checked

    Returns:
        (bool): True if the number mod 5 is 0, False otherwise
    """
    return not number % 5


def mod_three(number) -> bool:
    """Returns a boolean that is oposite of the
    passed number module with 3.

    Args:
        number (int): The number to be checked

    Returns:
        (bool): True if the number mod 3 is 0, False otherwise
    """
    return not number % 3


def main():
    count: int = 1

    while True:
        if mod_five(count) and mod_three(count):
            print("FIZZBUZZ", count)
        elif mod_five(count) and not mod_three(count):
            print("BUZZ", count)
        elif not mod_five(count) and mod_three(count):
            print("FIZZ", count)
        elif not mod_five(count) and not mod_three(count):
            print(count)

        if count == 30:
            break

        count = increase_number(count)


if __name__ == "__main__":
    main()
