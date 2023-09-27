#!/usr/bin/env /usr/bin/python3




def factorize_all(line):
    if line <= 1:
        return None, None
    if line % 2 == 0:
        if is_prime(line // 2):
            print("{}={}*{}".format(line, line // 2, 2))
            return
    else:
        for i in range(3, line, 2):
            if line % i == 0:
                if is_prime(line // i):
                    print("{}={}*{}".format(line, line // i, i))
                    return
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