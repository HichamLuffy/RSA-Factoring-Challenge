#!/usr/bin/env /usr/bin/python3

def read_and_print_file(file_path):
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
    return None


def factorize_all(line):
    for i in range(2, line):
        if line % i == 0:
            return i, line // i 
    return None
