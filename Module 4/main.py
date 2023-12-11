# Module 4 - Portfolio Milestone - Charles Henrikson
import ItemToPurchase

cart = []

print("Please enter two shopping cart item's names, prices and quantities:\n")

# Capture the items
for item in range(1, 3):
    print('Item ' + str(item))
    i_name = input("Enter the item name:")
    i_price = float(input("Enter the item price:"))
    i_quantity = int(input("Enter the item quantity:"))
    cart.append(ItemToPurchase.Item(i_name, i_price, i_quantity))

# Calculate total for cart
total = 0.00
for cart_item in cart:
    total = total + cart_item.item_price * cart_item.item_quantity

# Print invoice
print('\n')
for cart_item in cart:
    cart_item.print_item_cost()

print("\nTotal: ${total:.2f}".format(total=total))
