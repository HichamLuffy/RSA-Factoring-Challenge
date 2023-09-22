#!/usr/bin/env /usr/bin/python3
import sys

def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    i, j = factorize_all(int(line)) 
                    print("{}={}*{}".format(line, j, i))
                    #print(f"{line} = {factors}", end='\n')
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")


def factorize_all(line):
    try:
        for i in range(2, 1000):
            if line % i == 0:
                return i, line // i
                #for j in range(2, i):
                    #if i % j == 0:
                        #return i, j
                # print("{} = {} * {}".format(line, i, i)) 
    except Exception as e:
        print(f"Error: {e}")