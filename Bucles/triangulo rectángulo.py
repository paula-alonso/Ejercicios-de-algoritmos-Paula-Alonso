heigth = int(input("Introduzca la altura del triangulo rectángulo: "))
for num in range(1,heigth+1,2):
    if num > 1:
        while num>1:
            print(num, end=" ")
            num = num-2
        print(num)
    else:
        print(num)