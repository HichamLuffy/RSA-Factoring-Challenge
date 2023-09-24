#!/usr/bin/env /usr/bin/python3

import sys

def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    n = line
                    if int(line) <= 1:
                        print(f"{n} is not factorizable (prime or 1)")
                    else:
                        factors = factorize_all(n)
                        if factors:
                            p, q = factors
                            print("{}={}*{}".format(n, q, p))
                        else:
                            print(f"{n} is not factorizable")
                else:
                    print(f"{line} is not a number")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    return None


def factorize_all(line):
    if line <= 1:
        return None, None
    if line % 2 == 0:
        return line // 2, 2
    else:
        for i in range(3, line, 2):
            if line % i == 0:
                    return line // i, i
    return None, None

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True