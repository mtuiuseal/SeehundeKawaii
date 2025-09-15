# Write a Python program:
# 1.to handle a ZeroDivisionError exception when dividing a number by zero.
def divide_numbers( x, y ):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")


numerator = 100
denominator = 0
divide_numbers(numerator, denominator)


# 2.that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input( prompt ):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Error: Invalid input, input a valid integer.")


n = get_integer_input("Input an integer: ")
print("Input value:", n)


# 3.that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_numeric_input( prompt ):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")


n1 = get_numeric_input("Input the first number: ")
n2 = get_numeric_input("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)


# 4.that executes an operation on a list and handles an IndexError exception if the index is out of range.
def test_index( data, index ):
    try:
        result = data[index]
        print("Result:", result)
    except IndexError:
        print("Error: Index out of range.")


nums = [1, 2, 3, 4, 5, 6, 7]
index = int(input("Input the index: "))
test_index(nums, index)


# 5.that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    n = int(input("Input a number: "))
    print("You entered:", n)
except KeyboardInterrupt:
    print("Input canceled by the user.")


# 6.that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def division( dividend, divisor ):
    try:
        result = dividend / divisor
        print("Result:", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")


dividend = float(input("Input the dividend: "))
divisor = float(input("Input the divisor: "))
division(dividend, divisor)
