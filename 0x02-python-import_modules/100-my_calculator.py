#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator == "+":
        result = add(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == "-":
        result = sub(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == "*":
        result = mul(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == "/":
        result = div(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
