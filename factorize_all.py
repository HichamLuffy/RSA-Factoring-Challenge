#!/usr/bin/env /usr/bin/python3
import math
import random
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    n = int(line)
                    if int(line) <= 1:
                        print(f"{n} is not factorizable (prime or 1)")
                    elif not is_prime(n):
                        factors = factorize_all(n)
                    if factors:
                            if len(factors) == 2:
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
    while line > 1:
        if line % 2 == 0:
            return 2, line // 2
        else:
            for i in range(3, line, 2):
                if line % i == 0:
                    factor = pollard_rho(i)
                    return factor, line // factor

def pollard_rho(n):
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
    return d


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True