'''
Write a class called CoffeeShop, which has three instance variables:

name : a string (basically, of the shop)
menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a food or a drink) and price.
orders : an empty list
and seven methods:

add_order: adds the name of the item to the end of the orders list if it exists on the menu, otherwise, return "This item is currently unavailable!"
fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty, return "All orders have been fulfilled!"
list_orders: returns the item names of the orders taken, otherwise, an empty list.
due_amount: returns the total amount due for the orders taken.
cheapest_item: returns the name of the cheapest item on the menu.
drinks_only: returns only the item names of type drink from the menu.
food_only: returns only the item names of type food from the menu.
IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order.

Examples
tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
# Tesha's coffee shop does not sell hot cocoa
tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
# specifying the variant of "iced tea" will help the process

tcs.add_order("cinnamon roll") ➞  "Order added!"
tcs.add_order("iced coffee") ➞ "Order added!"
tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
# all items of the current order

tcs.due_amount() ➞ 2.17

tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
tcs.fulfill_order() ➞ "The iced coffee is ready!"
tcs.fulfill_order() ➞ "All orders have been fulfilled!"
# all orders have been presumably served

tcs.list_orders() ➞ []
# an empty list is returned if all orders have been exhausted

tcs.due_amount() ➞ 0.0
# no new orders taken, expect a zero payable

tcs.cheapest_item() ➞ "lemonade"
tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee"]
tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg",
'''


class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
        self.order_price = 0

    def add_order(self, order_name):
        # temp = (map(lambda order: (True if order_name in order['item'] else False), self.menu))
        # print(temp)
        # if True in temp:
        #     self.orders.append(order_name)
        #     print("Order added!")
        # else:
        #     print("This item is currently unavailable!")
        ###############################################################
        for order in self.menu:
            if order_name in order['item']:
                self.orders.append(order_name)
                self.order_price += order['price']
                print("Order added!")
                break

    def fulfill_order(self):
        try:
          if (len(self.orders) == 0):
             raise ValueError("All orders have been fulfilled!")
        except ValueError as e:
            print(e)
        else:
            current_order = self.orders.pop(0)
            print("The {} is ready!".format(current_order))

    def list_orders(self):
        return self.orders

    def due_amount(self):
        pass

    def cheapest_item(self):
        pass

    def drinks_only(self):
        pass

    def food_only(self):
        pass


m1, m2, m3 = [["orange juice", "drink", 2.13], ["lemonade", "drink", 0.85],
              ["cranberry juice", "drink", 3.36], ["pineapple juice", "drink", 1.89],
              ["lemon iced tea", "drink", 1.28], ["apple iced tea", "drink", 1.28],
              ["vanilla chai latte", "drink", 2.48], ["hot chocolate", "drink", 0.99],
              ["iced coffee", "drink", 1.12], ["tuna sandwich", "food", 0.95],
              ["ham and cheese sandwich", "food", 1.35], ["bacon and egg", "food", 1.15],
              ["steak", "food", 3.28], ["hamburger", "food", 1.05],
              ["cinnamon roll", "food", 1.05]], [["turkey english muffin", "food", 7.99],
                                                 ["avocado toast", "food", 5.05],
                                                 ["chocolate croissant", "food", 3.00],
                                                 ["espresso", "drink", 2.99],
                                                 ["iced caramel macchiato", "drink", 4.50],
                                                 ["cortado", "drink", 4.00],
                                                 ["nitro cold brew tester", "drink", 8.00]], [
                 ["cheeseburger with fries", "food", 5.44], ["cinnamon roll", "food", 4.99],
                 ["hot chocolate", "drink", 2.99], ["lemon tea", "drink", 2.50],
                 ["iced coffee", "drink", 3.00], ["vanilla chai latte", "drink", 4.00]]
menu1 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m1]
menu2 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m2]
menu3 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m3]

shopx = CoffeeShop("Xavier's", menu1, list())
shopx.add_order("steak")
print(shopx.order_price)
shopx.add_order("vanilla chai latte")
shopx.fulfill_order()
shopx.fulfill_order()
shopx.fulfill_order()

print(shopx.order_price)  # shopx.add_order("vanilla chai latte")
# print(shopx.orders)
