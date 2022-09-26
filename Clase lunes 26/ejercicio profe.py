num = input ("Introduzca un número entero: ")
if num.isnumeric():
    num = int (num)
    for num_for in range (1, num+1, 2):
        aux = num_for
        while aux>=1:
            if aux == 1:
                print(aux)
            else:
                print(aux,end=" ")
            
            aux-=2
        
else:
    print("Cifra inválida")