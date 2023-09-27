#!/usr/bin/env /usr/bin/python3

def factorize_all(line):
    if line <= 1:
        return None, None
    for i in range(2, int(line**0.5) + 1):
        if line % i == 0:
            print("{}={}*{}".format(line, line // i, i))
            return
    return None, None
