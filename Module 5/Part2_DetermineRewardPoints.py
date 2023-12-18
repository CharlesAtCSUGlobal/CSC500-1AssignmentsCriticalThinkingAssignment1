# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month.
# The points are awarded as follows:
#
#     If a customer purchases 0 books, they earn 0 points.
#     If a customer purchases 2 books, they earn 5 points.
#     If a customer purchases 4 books, they earn 15 points.
#     If a customer purchases 6 books, they earn 30 points.
#     If a customer purchases 8 or more books, they earn 60 points.
#
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.


print("Welcome to CSU Global Bookstore Book Club Rewards!\n")

number_of_books = int(input("How many books were purchased this month? "))

number_of_points = 0
if 2 <= number_of_books < 4:  # If a customer purchases 2 books, they earn 5 points.
    number_of_points = 5
elif 4 <= number_of_books < 6:  # If a customer purchases 4 books, they earn 15 points.
    number_of_points = 15
elif 6 <= number_of_books < 8:  # If a customer purchases 6 books, they earn 30 points.
    number_of_points = 30
elif number_of_books >= 8:  # If a customer purchases 8 or more books, they earn 60 points.
    number_of_points = 60

print("Points awarded: {}".format(number_of_points))
