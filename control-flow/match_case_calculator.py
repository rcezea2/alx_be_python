#!/usr/bin/python3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ")


def do_math(operation, a, b):
    result = 'The result is {}.'

    match operation:
        case '+':
            return a + b

        case '-':
            return a - b

        case '*':
            return a * b

        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                return a / b


print('The result is {}.'.format(do_math(op, num1, num2)))
