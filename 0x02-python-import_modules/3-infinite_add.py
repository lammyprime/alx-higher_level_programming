#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_sum = 0
    for argc in range(1, len(argv)):
        arg_num = int(argv[argc])
        arg_sum += arg_num
    print(arg_sum)
