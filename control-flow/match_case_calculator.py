#!/usr/bin/python3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ")


def do_math(operation, a, b):
    result = 'The result is {}'

    match operation:
        case '+':
            print(result.format(a + b))

        case '-':
            print(result.format(a - b))

        case '*':
            print(result.format(a * b))

        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(result.format(a / b))


do_math(op, num1, num2)
