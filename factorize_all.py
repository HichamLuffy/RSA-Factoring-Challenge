#!/usr/bin/env /usr/bin/python3
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    n = int(line)
                    factorize_all(n)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    return None


def factorize_all(line):
    if line <= 1:
        return None, None
    if line % 2 == 0:
        print("{}={}*{}".format(line, line // 2, 2))
        return line // 2, 2
    else:
        for i in range(3, line, 2):
            if line % i == 0:
                    print("{}={}*{}".format(line, line // i, i))
                    return line // i, i
    return None, None
