#!/usr/bin/env python3
"""main.py"""
import os


def read_file(filename: str) -> object:
    """Read in a file and return it's lines in a
    list with the newline characters sripped off

    Args:
        filename (str): The path and name of the file

    Raises:
        fnfe: Raised if the file does not exist

    Returns:
        list[str]: List of the the read files lines
    """

    file_lines = []

    try:
        with open(filename, encoding="utf-8") as read:
            raw_lines = read.readlines()
    except FileNotFoundError as fnfe:
        raise fnfe
    else:
        for line in raw_lines:
            file_lines.append(line.rstrip())

    return file_lines


def main() -> None:
    """main"""
    print("Hello, world!")


if __name__ == "__main__":
    os.system("clear")

    main()
