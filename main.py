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

    try:
        with open(filename, encoding="utf-8") as read:
            raw_lines = read.readlines()
    except FileNotFoundError as fnfe:
        raise fnfe

    for i, line in enumerate(raw_lines):
        raw_lines[i] = line.replace(line[-1], "")

    return raw_lines


def main() -> None:
    """main"""
    files_name: str = os.path.expanduser(os.path.join("~", "ed", "fizbuz", "cats.sh"))
    readme_lines = read_file(files_name)

    for line in readme_lines:
        print(line)


if __name__ == "__main__":
    os.system("clear")

    main()
