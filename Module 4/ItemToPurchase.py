# ItemToPurchase.py
# Module 4 - Portfolio Milestone - Charles Henrikson
#
#    Attributes
#      item_name (string)
#      item_price (float)
#      item_quantity (int)
#    Default constructor
#       Initializes item's name = "none", item's price = 0, item's quantity = 0
#    Method
#      print_item_cost()


class Item:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_quantity * self.item_price
        print('{name} {quantity} @ ${price:.2f} = ${total:.2f}'.format(name=self.item_name, quantity=self.item_quantity, price=self.item_price, total=total))
