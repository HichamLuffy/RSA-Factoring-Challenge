#!/usr/bin/env /usr/bin/python3
import math
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    n = int(line)
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
    if line % 2 == 0:
        p = 2
        q = line // 2
    else:
        for i in range(3, int(math.gcd(line)), 2):
            if line % i == 0:
                p = i
                q = line // i
                break
            

    return p, q
