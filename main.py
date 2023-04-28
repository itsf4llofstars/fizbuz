#!/usr/bin/env python
import os
import sys


def say_hi(string: str) -> None:
    print(f"Hello, {string}")


def main():
    name: str = "Harley"
    say_hi(name)


if __name__ == "__main__":
    os.system("clear")

    sys.exit(main())
