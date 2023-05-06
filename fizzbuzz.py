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
    return not number % 5


def mod_three(number) -> bool:
    return not number % 3


def main():
    count: int = 0

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
