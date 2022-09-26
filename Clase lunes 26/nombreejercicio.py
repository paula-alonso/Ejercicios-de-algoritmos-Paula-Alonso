num = (input("Introduzca un número: "))
if num.isnumeric():
    num = int (num)
    for num_for in range(1,num+1,2):
        if num_for>=num-1:
            print(num_for)
        else:
            print(num_for, end=",")
else:
    print("Cifra inválida")






