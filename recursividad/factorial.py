num = 3
def get_factorial(num):
    if num == 1:
        return 1
    return num * get_factorial(num-1)

print(get_factorial(num))