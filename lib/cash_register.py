#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

@property
def dicount(self):
    return self._discount

@dicount.setter
def dicount(self, value):
    if type(value) is int and 0 <= value <= 100:
        self._discount = value
    else:
        print("Not valid discount")

def add_item(self, item, price, quantity):
    new_item = {
       'item': item,
       'price': price,
       'quantity': quantity
    }
    self.price = price * quantity
    self.items.append(new_item)
    self.total += self.price  
    self.previous_transactions.append(new_item)