class Books:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def UsarLibro(self):
        libro = (self.name, self.type)
        return libro
