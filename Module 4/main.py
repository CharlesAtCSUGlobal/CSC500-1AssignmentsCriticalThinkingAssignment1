
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_quantity * self.item_price
        print('{name} {quantity} @ ${price:.2f} = ${total:.2f}'.format(name=self.item_name, quantity=self.item_quantity, price=self.item_price, total=total))

cart = []

print("Please enter two shopping cart item's names, prices, and quantities:\n")

# Capture the items
for item in range(1, 3):
    print('Item ' + str(item))
    i_name = input("Enter the item name:")
    i_price = float(input("Enter the item price:"))
    i_quantity = int(input("Enter the item quantity:"))
    cart.append(ItemToPurchase(i_name, i_price, i_quantity))

# Calculate total for cart
total = 0.00
for cart_item in cart:
    total = total + cart_item.item_price * cart_item.item_quantity

# Print invoice
print('\n')
for cart_item in cart:
    cart_item.print_item_cost()

print("\nTotal: ${total:.2f}".format(total=total))
