
lista = {9,2,8,1,15,12,3}
#Seleccion
def ordenar(lista):
    cant = len(lista)
    for elemento in range(cant):
        index_menor = elemento
        for elemento2 in range(elemento+1, cant):
            if lista[index_menor] > lista[elemento2]:
                index_menor = elemento2
        lista[elemento], lista[index_menor] = lista[index_menor], lista[elemento]

print(lista)

#Busqueda binaria

def busqueda(lista, cosa, nombre_cosa_buscar = 5):
    if len(lista) == 0:
        return None
    mitad = len(lista)//2
    if lista[mitad].get(nombre_cosa_buscar) is not None:
        if lista[mitad][nombre_cosa_buscar] == cosa:
            return lista[mitad]
        elif cosa < lista[mitad][nombre_cosa_buscar]:
            return busqueda(lista[0:mitad], cosa, nombre_cosa_buscar)
        else:
            return busqueda(lista[mitad: 0], cosa, nombre_cosa_buscar)


            
