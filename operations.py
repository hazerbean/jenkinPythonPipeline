def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:

        return "Zero Division Error!"


def power(a, b):
    return "Power operation is not supported."
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero Division Error"

