num = int(input("Introduzca un número natural: "))
#con while
aux = num
while aux>=0:
    if aux == 0:
        print(aux)
    else:
        print(aux, end=",")
    aux-=1
#con for
for nums in range(0, num+1):
    if nums-num == 0:
        print(abs(nums-num))
    else:
        print(abs(nums-num), end=",")