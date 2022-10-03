#Con while
num = input("Introduzca un número entero positivo: ")
if num.isnumeric() and int(num) != 0:
    num = int(num)
    aux = 1
    while aux<=num:
        if aux >= num-1:
            print(aux)
        else:
            print(aux, end=",")
        aux+=2

    #Con for
    for nums in range(1, num+1, 2):
        if nums >= num-1:
            print(nums)
        else:
            print(nums, end=",")
else:
    print("Introduzca una cifra válida")

