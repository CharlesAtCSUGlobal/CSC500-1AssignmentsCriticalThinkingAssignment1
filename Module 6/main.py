from datetime import date


class ShoppingCart:

    # Attributes
    #    customer_name (string) - Initialized in default constructor to "none"
    #    current_date (string) - Initialized in default constructor to "January 1, 2020"
    #    cart_items (list)

    # Parameterized constructor, which takes the customer name and date as parameters
    def __init__(self, customer_name='none', current_date=date.today()):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Methods
    #   add_item()
    #       Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print("\nItem {} added.\n".format(item_to_purchase.item_name))

    #   remove_item()
    #       Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    #       If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        item_found = False
        for i in self.cart_items:
            if i.item_name == item_name:
                item = self.cart_items.remove(i)
                item_found = True
        if item_found:
            print("{} removed.".format(item_name))
        else:
            print("\nItem not found in cart. Nothing removed.\n")

    #   modify_item()
    #       Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    #       If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    #       If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_to_purchase):
        print("Modify Item -- Not implemented yet")
        # print("Item not found in cart. Nothing removed.")

    #   get_num_items_in_cart()
    #       Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        item_count = 0
        for item in self.cart_items:
            item_count = item_count + item.item_quantity
        return item_count

    #   get_cost_of_cart()
    #        Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total = 0.00
        for item in self.cart_items:
            total = total + item.item_price * item.item_quantity
        return total

    #    print_total()
    #       Outputs total of objects in cart.
    #       If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}\nNumber of Items: {}".format(self.customer_name, self.current_date,
                                                                    self.get_num_items_in_cart()))
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: ${total:.2f}".format(total=self.get_cost_of_cart()))

    # print_descriptions()
    #        Outputs each item's description.
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\nItem Descriptions".format(self.customer_name, self.current_date))
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = item_description

    def print_item_cost(self):
        total = self.item_quantity * self.item_price
        print('{name} {quantity} @ ${price:.2f} = ${total:.2f}'.format(name=self.item_name, quantity=self.item_quantity,
                                                                       price=self.item_price, total=total))


def print_menu():
    print('''MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit''')


# Main
customer_name = input("Enter the Customer name:")
shopping_cart = ShoppingCart(customer_name)

menu_choice = ""
while menu_choice.lower() != "q":
    print_menu()
    menu_choice = input("Choose an option:")
    if menu_choice.lower() == "a":
        i_name = input("Enter the item name:")
        i_description = input("Enter the item description:")
        i_price = float(input("Enter the item price:"))
        i_quantity = int(input("Enter the item quantity:"))
        shopping_cart.add_item(ItemToPurchase(i_name, i_price, i_quantity, i_description))
        print("{} item(s) in cart.".format(shopping_cart.get_num_items_in_cart()))
    elif menu_choice.lower() == "r":
        i_name = input("Enter the item name to remove:")
        shopping_cart.remove_item(i_name)
    elif menu_choice.lower() == "c":
        print("c was chosen")
    elif menu_choice.lower() == "i":
        print("i was chosen")
    elif menu_choice.lower() == "o":
        shopping_cart.print_total()
    elif menu_choice.lower() != "q":
        print("Unknown Option, Please try again.\n")
print("Exiting program...")
