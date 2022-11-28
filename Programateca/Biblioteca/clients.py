from http import client
from unicodedata import name


class Client:
    def __init__(self, name, ci):
        self.name = name
        self.ci = ci
    def GuardarCliente(self):
        cliente = (self.name, self.ci)
        return cliente
