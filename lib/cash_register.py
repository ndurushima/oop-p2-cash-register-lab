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

