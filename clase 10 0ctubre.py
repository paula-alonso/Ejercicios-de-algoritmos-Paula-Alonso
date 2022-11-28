#Libreria math
def print_welcome():
    print("Welcome")
def get_option(studies):
    for key, value in studies.items():
        for keyinterno, valueinterno in value.items():
            print(f"{key}-{valueinterno}", end=" ")
        print("")
    return input("Please enter an option: ")
def get_cliente_data(study):
    client = {"id": input("Enter your id"), "age": input("Enter your age: "), "gender": input("Enter your gender: "), "study": study}
def main():
    studies_dict = {"U": {"Description": "Ultrasonido", "price": 8900}, "I": {"Description": "Infografía", "price": 12640}}
    print_welcome()
    option = get_option(studies_dict)

main()