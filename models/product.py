class Product:

  def __init__(self, name, product_id, price, category, quantity = 0, minimum_stock = 5):
    self.name = name
    self.product_id = product_id
    self.price = price
    self.category = category
    self.quantity = quantity
    self.minimum_stock = minimum_stock

  def __str__(self):
    return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nCategory: {self.category}"

  def add_stock(self, quantity):
    if type(quantity) == int and quantity > 0:
      self.quantity += quantity
      return f"You have successfully added {quantity} of this product"
    else:
      return 'Wrong input!' 

  def remove_stock(self, quantity):
    if type(quantity) == int and self.quantity >= quantity and quantity > 0:
      self.quantity -= quantity
      return f"You have successfully removed {quantity} of this product."
    else:
      return "You can't remove this number of product, try again."

  def is_stock_low(self):
    return self.quantity <= self.minimum_stock


product_1 = Product('Iphone', 'P001', 2000, 'Electronics')
product_2 = Product('Bag', 'P002', 100, 'School')
product_3 = Product('Laptop', 'P003', 3000, 'Electronics')
product_4 = Product('Microwave', 'P004', 500, 'Utensils')
product_5 = Product('Wristwatch', 'P005', 200, 'Fashion')

