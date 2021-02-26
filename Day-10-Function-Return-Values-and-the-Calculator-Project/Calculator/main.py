# Calculator Program
import art
from replit import clear


# Add
def add(number1, number2):
    """Takes 2 numbers and returns their sum"""
    return (number1 + number2)


# Subtract
def subtract(number1, number2):
    """Takes 2 numbers and returns their difference"""
    return (number1 - number2)


# Multiply
def multiply(number1, number2):
    """Takes 2 numbers and returns their product"""
    return (number1 * number2)


# Divide
def divide(number1, number2):
    """Takes 2 numbers and returns their division"""
    return (number1 / number2)


def calculator():
    print(art.logo)

    operations = {
                '+' : add,
                '-': subtract,
                '*': multiply,
                '/': divide
                }

    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        calculate = operations[operator]
        answer = calculate(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        restart = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to exit.: ").lower()

        if restart == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()