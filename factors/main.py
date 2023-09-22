#!/usr/bin/python3
from factorize_all import read_and_print_file
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    read_and_print_file(file_path)