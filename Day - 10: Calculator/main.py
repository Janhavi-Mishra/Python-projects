#Project - calculator
import art

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1,n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

#dictionary with functions
operators = {
    '+': add,
    '-': subtract, 
    '*': multiply, 
    '/': divide,
    }

#calculator function
def calculator():
    print(art.logo)
    num1 = float(input("First number: "))
    for function in operators:
            print(function)

    should_continue = True
    while should_continue == True:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("next number: "))

        operation = operators[operator_symbol]
        result = float("{:.3f}".format(operation(num1,num2)))

        print(f"\n{num1} {operator_symbol} {num2} = {result}\n")

        repeat = input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation: ").lower()

        if repeat != 'y':
            should_continue = False
            calculator()    #recursions within a function
        else:
            num1 = result

calculator()
