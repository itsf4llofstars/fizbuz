#!/usr/bin/env python3
"""main.py"""
import os


def read_file(filename: str) -> object:
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
