class Vendedor:
    def __init__(self, product, id, amnt):
        self.product = product
        self.id = id
        self.amnt = amnt
    def mostrar(self):   
        print(f"Product id: {self.product}\nCustomer id: {self.id}\nAmnt: {self.amnt}")    