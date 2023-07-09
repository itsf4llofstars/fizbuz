#!/usr/bin/env python
import os


def read_full_file(filename: str):
    """Read in an entire file and return each line as a list

    Args:
        filename (str): The path and filename to be read

    Returns
        (List[str]): A list of string each being one line
                     of the read file
    """

    file_lines = []

    try:
        with open(filename, encoding="utf-8") as read:
            lines = read.readlines()
    except FileNotFoundError as fnfe:
        raise fnfe
    else:
        for line in lines:
            file_lines.append(line.rstrip())

    return file_lines


def main():
    """main"""
    file_name = os.path.expanduser(os.path.join("~", "ed", "file.txt"))
    files_lines = read_full_file(file_name)

    for line in files_lines:
        print(line)

    print()

    [print(line) for line in files_lines]


if __name__ == "__main__":
    main()
