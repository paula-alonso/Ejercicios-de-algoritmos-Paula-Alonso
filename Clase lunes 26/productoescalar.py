vect1 = [1, 2, 3]
vect2 = [-1, 0, 2]
acum = 0
for index in range(len(vect1)):
    acum += (vect1[index]*vect2[index])
    print(acum)