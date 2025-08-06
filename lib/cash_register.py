class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    new_item = {
      'item': item,
      'price': price * quantity,
      'quantity': quantity
    }
    self.previous_transactions.append(new_item)

    for _ in range(quantity):
      self.items.append(item)

    self.total += new_item['price'] 

  def apply_discount(self):
    if self.discount == 0:
        print("There is no discount to apply.")
        return
    discount_amount = self.total * (self.discount / 100)
    self.total -= discount_amount
    return self.total
      
  def void_last_transaction(self):
    if not self.previous_transactions:
        print("There is no transaction to void.")
        return
    last = self.previous_transactions.pop()
    self.total -= last['price']
    for _ in range(last['quantity']):
        self.items.remove(last['item'])
    self.total -= last['price']
    return self.total

