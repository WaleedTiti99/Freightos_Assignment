class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def purchase_product(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            print("{} is out of stock!".format(self.name))
            return False

    def __str__(self):
        return str("{} which is ${}".format(self.name, self.price))
