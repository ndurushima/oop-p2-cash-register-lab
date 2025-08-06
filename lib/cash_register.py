class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    new_item = {
      'item': item,
      'price': price,
      'quantity': quantity
    }
    self.price = price * quantity
    self.items.append(new_item)
    self.total += self.price  
    self.previous_transactions.append(new_item)

  def apply_discount(self):
    self.total -= self.total * (self.discount / 100)
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

