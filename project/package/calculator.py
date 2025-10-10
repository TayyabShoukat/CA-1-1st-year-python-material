#functions with default parameters and no return value
def sum(firstNumber=0,secondNumber=0,thirdNumber=0):
    print("Sum is",firstNumber+secondNumber+thirdNumber)

def subtract(firstNumber=0,secondNumber=0):
    print("Subtraction is",firstNumber-secondNumber)

def multiply(firstNumber=1,secondNumber=1):
    print("Multiplication is",firstNumber*secondNumber)

def divide(firstNumber=1,secondNumber=1):
    if secondNumber != 0:
        print("Division is",firstNumber/secondNumber)
    else:
        print("Error: Division by zero is not allowed.")
