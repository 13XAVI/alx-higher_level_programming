#!/usr/bin/python3
if __name__ == "__main__":
    """print sum,multiply,difference,divide"""
from calculator_1 import add, substract, multiply, divide
a = 10
b = 5


print("{}+{} = ".format(a, b), add(10, 5))
print("{}-{} = ".format(a, b), substract(10, 5))
print("{}*{} = ".format(a, b), multiply(10, 5))
print("{}/{} = ".format(a, b), divide(10, 5))
