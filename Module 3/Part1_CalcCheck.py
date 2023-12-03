# Charles Henrikson
#
# 23WA-CSC500-1
# Module 3: Critical Thinking Assignment
# Part 1:
#
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the
# user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales
# tax. Display each of these amounts and the total price.

print("Welcome to Bill Prep!")
cart = []
more_items = True

# Collect Data
while more_items:
    if more_items:
        food_item = input("Add Food Item: ")
        food_price = float(input("Price: "))
        food_quantity = int(input("Quantity: "))
        cart.append({
            'item_name': food_item,
            'item_price': food_price,
            'item_quantity': food_quantity
        })
    more_food_response = input("Add More Food? (y/n): ")
    if more_food_response == 'n' or more_food_response == 'N':
        more_items = False

# Calculate Bill
cart_sum = 0
for item in cart:
    cart_sum += item["item_price"] * item["item_quantity"]

# Calculate Gratuity
gratuity = cart_sum * 0.18
tax = cart_sum * 0.07
total_owed = cart_sum + gratuity + tax

# Print Bill
print("------------ Food Bill --------------\n")

print("Purchased: \n")

for item in cart:
    print('   {quantity} {name} @ ${price:.2f}'.format(name=item["item_name"],
                                                       quantity=item["item_quantity"],
                                                       price=item["item_price"] )
          )
print('   -----------------------')
print('Sub Total:     ${0:.2f}'.format(cart_sum))
print(' 7% Sales Tax: ${0:.2f}'.format(tax))
print('18% Gratuity:  ${0:.2f}'.format(gratuity))
print('   -----------------------')
print('Final Total:   ${0:.2f}'.format(total_owed))
print("\n\n-- Thanks for Eating at Charles's --")
