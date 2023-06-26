#!/usr/bin/env python3
"""main.py"""
import os


def read_file(filename: str):
    """Read in an entire file and return a list of each
    file line

    Args:
        filename (str): The path and filename to be read

    Returns:
        (List[str]): A list of strings each being one
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

    if file_lines:
        return file_lines
    return None


def main():
    file_name = os.path.expanduser(os.path.join("~", "ed", "fizbuz", "main.py"))
    files_lines = read_file(file_name)
    [print(line) for line in files_lines]


if __name__ == "__main__":
    main()
