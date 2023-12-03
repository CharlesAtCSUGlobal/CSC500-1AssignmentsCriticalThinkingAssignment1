# Part 2:
# Write a Python program to find the multiplication and division of two numbers.
#   Ask the user to input two numbers (num1 and num2).
#       Given those two numbers, multiply them together to find the output.
#       Also, divide num1/num2 to find the output.

# Part 2
num1 = int(input('Enter a number:\n'))
num2 = int(input('Enter a non-zero number:\n'))
# If num2 is a 0, this will cause an error -- we should resolve this in the future
print("You entered: " + str(num1) + ' and ' + str(num2))
print(str(num1) + ' * ' + str(num2) + " = " + str(num1 * num2))
print(str(num1) + ' / ' + str(num2) + " = " + str(num1 / num2))
