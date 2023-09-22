#!/usr/bin/env /usr/bin/python3
import sys

def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    if int(line) <= 1:
                        continue
                    i, j = factorize_all(int(line)) 
                    print("{}={}*{}".format(line, j, i))
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    return None


def factorize_all(line):
    try:
        for i in range(2, line):
            if line % i == 0:
                return i, line // i 
    except Exception as e:
        print(f"Error: {e}")
    return None
