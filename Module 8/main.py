from datetime import date


class ShoppingCart:

    def __init__(self, customer_name='none', cart_date=date.today().strftime("%b %d, %Y")):
        self.customer_name = customer_name
        self.current_date = cart_date
        self.cart_items = []

    # Methods

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print("\nItem {} added.\n".format(item_to_purchase.item_name))

    def find_item(self, item_name):
        item = None
        for i in self.cart_items:
            if i.item_name.lower() == item_name.lower():
                item = i
                break
        return item

    def remove_item(self, item_name):
        item_found = False
        for i in self.cart_items:
            if i.item_name.lower() == item_name.lower():
                self.cart_items.remove(i)
                item_found = True
        if item_found:
            print("{} removed.\n".format(item_name))
        else:
            print("\nItem not found in cart. Nothing removed.\n")

    def modify_item(self, item_to_purchase):
        i: ItemToPurchase
        for i in self.cart_items:
            if i.item_name.lower() == item_to_purchase.item_name.lower():
                self.cart_items.remove(i)
                self.cart_items.append(item_to_purchase)
            print("{} modified.\n".format(item_to_purchase.item_name))

    def get_num_items_in_cart(self):
        item_count = 0
        for item in self.cart_items:
            item_count = item_count + item.item_quantity
        return item_count

    def get_cost_of_cart(self):
        total = 0.00
        for item in self.cart_items:
            total = total + item.item_price * item.item_quantity
        return total

    def print_cart_description(self):
        print("Customer name: {}\nToday's date: {}".format(self.customer_name, self.current_date))

    def print_item_names(self):
        for item in self.cart_items:
            print(item.item_name)

    def print_total(self):
        print("{}'s Shopping Cart - {}\nNumber of Items: {}".format(self.customer_name, self.current_date,
                                                                    self.get_num_items_in_cart()))
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: ${total:.2f}\n".format(total=self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\nItem Descriptions".format(self.customer_name, self.current_date))
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))
        print()


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

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
customer = input("Enter the Customer name:")
current_date = date.today()
date_in = input("Enter today's date [{}]:".format(current_date.strftime("%b %d, %Y")))
if date_in == "":
    date_in = current_date.strftime("%b %d, %Y")
shopping_cart = ShoppingCart(customer, date_in)
shopping_cart.print_cart_description()

menu_choice = ""
while menu_choice.lower() != "q":
    print_menu()
    menu_choice = input("Choose an option:")

    if menu_choice.lower() == "a":
        try:
            i_name = input("Enter the item name:")
            if len(i_name) == 0:
                raise ValueError("Name can not be blank, please try again.")
            i_description = input("Enter the item description:")
            i_price = float(input("Enter the item price:"))
            i_quantity = int(input("Enter the item quantity:"))
            shopping_cart.add_item(ItemToPurchase(i_name, i_price, i_quantity,
                                                  i_description))
            print("{} item(s) in cart.\n".format(shopping_cart.get_num_items_in_cart()))
        except ValueError:
            print("\nThere was an error, please try again.")

    elif menu_choice.lower() == "r":
        print("\nREMOVE ITEM FROM CART")
        if shopping_cart.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY\n")
        else:
            shopping_cart.print_item_names()
            i_name = input("Enter the item name to remove:")
            shopping_cart.remove_item(i_name)
            print("{} item(s) in cart.\n".format(shopping_cart.get_num_items_in_cart()))

    elif menu_choice.lower() == "c":
        print("\nCHANGE ITEM QUANTITY")
        if shopping_cart.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY\n")
        else:
            shopping_cart.print_item_names()
            i_name = input("Enter the item name to update:")
            i_quantity = 0
            l_item = shopping_cart.find_item(i_name)
            try:
                if l_item is None:
                    print("\nItem not found in cart. Nothing modified.\n")
                else:
                    i_quantity = int(input("Enter the new quantity:"))
                    new_item = ItemToPurchase(l_item.item_name, l_item.item_price,
                                              i_quantity, l_item.item_description)
                    shopping_cart.modify_item(new_item)
                    print("{} item(s) in cart.\n".format(shopping_cart.get_num_items_in_cart()))
            except ValueError:
                print("\nThere was an error, please try again.")

    elif menu_choice.lower() == "i":
        if shopping_cart.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY\n")
        else:
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

    elif menu_choice.lower() == "o":
        if shopping_cart.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("\nOUTPUT SHOPPING CART")
            shopping_cart.print_total()

    elif menu_choice.lower() != "q":
        print("\nUnknown Option, Please try again.\n")

print("Exiting program...")
