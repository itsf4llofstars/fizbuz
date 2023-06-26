#!/usr/bin/env python3
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
    finally:
        if file_lines:
            return file_lines


def main():
    file_name = os.path.expanduser(os.path.join("~", "ed", "file.txt"))
    files_lines = read_full_file(file_name)
    [print(line) for line in files_lines]


if __name__ == "__main__":
    main()
