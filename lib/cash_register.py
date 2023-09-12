#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity = 1):
        last_transaction = price * quantity
        self.total += last_transaction
        for x in range(quantity):
            self.items.append(title)
        self.last_transaction.append({"title": title, "quantity": quantity, "price":price })

    def apply_discount(self):
        self.total = self.total * (1 - (self.discount/100))
        if (int(self.total) == 0):
            print("There is no discount to apply.")
        else:
            print(f'After the discount, the total comes to ${int(self.total)}.')

    def void_last_transaction(self):
        self.total = self.total - (self.last_transaction[-1]["price"]*self.last_transaction[-1]["quantity"])