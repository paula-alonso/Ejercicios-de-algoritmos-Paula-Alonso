class Producto:
    def __init__(self, id, name, type, stock):
        self.id = id
        self.name = name
        self.type = type
        self.stock = stock
    
class Flores(Producto):
    def __init__(self, id, name, type, stock, colors):
        super().__init__(id, name, type, stock)
        self.colors = colors
    def mostrar(self):
        print(f"Id: {self.id}\nName: {self.name}\nType: {self.type}\nStock: {self.stock}")
        print("Colors:", end=" ")
        for element in self.colors:
            print(element)
class Semillas(Producto): 
    def __init__(self, id, name, type, stock, colors):
        super().__init__(id, name, type, stock)
        self.colors = colors
    def mostrar(self):
        if self.colors == None:
            print(f"Id: {self.id}\nName: {self.name}\nType: {self.type}\nStock: {self.stock}")
        else:
            print(f"Id: {self.id}\nName: {self.name}\nType: {self.type}\nStock: {self.stock}")
            print("Colors:", end=" ")
            for element in self.colors:
                print(element)
    
