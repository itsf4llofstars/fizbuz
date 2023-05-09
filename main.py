#!/usr/bin/env python
import os


def read_full_file(filename: str):
    """Read in an entire file and return each line in a list

    Args:
        filename (str): The path and filename to be read

    Returns (List[str]): A list of string each being one
                         line of the read file
    """
    file_lines = []
    try:
        with open(filename, encoding="utf-8") as read:
            lines = read.readlines()
    except FileNotFoundError as fnfe:
        print(f"ERROR: {fnfe}")
    else:
        for line in lines:
            file_lines.append(line.rstrip())


def main():
    pass


if __name__ == "__main__":
    main()
