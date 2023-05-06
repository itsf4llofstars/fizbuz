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


def main():
    count: int = 0


if __name__ == "__main__":
    main()
