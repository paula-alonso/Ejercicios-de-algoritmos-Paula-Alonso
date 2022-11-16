def main():
    list = ["a", "b", "c"]
    user = input("Introduce una letra: ")
    def get_letra(list, user,index = 0):
        if user == list[index]:
            return user
        else:
            if index == len(list)-1:
                if user == list[index]:
                    return user
                else:
                    return None
        return get_letra(list, user, index+1)


