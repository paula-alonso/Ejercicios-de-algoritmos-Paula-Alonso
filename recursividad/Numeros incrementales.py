num = input("Introduzca un número natural: ")

i = 0    
def num_incremental(num, i):
    if i == len(num)-1:
        return True
    if num[i] > num[i+1]:
        return False
    return num_incremental(num, i+1)

if num_incremental (num, i) == False:
    print(f"El número {num} no es incremental")

else:
    print(f"El número {num} es incremental")
    
    
    
    