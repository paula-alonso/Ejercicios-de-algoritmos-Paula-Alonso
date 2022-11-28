from Redactores import Redactores, Jefes
from seccion import Seccion
def get_redactores_entreteimiento():
    return [Redactores["Leo",1234], Redactores["Ana",1234],Redactores["Julia",1234]]
def get_redactores_farandula():
    return [Redactores["Leo",1234], Redactores["Ana",1234],Redactores["Julia",1234]]
def get_redactores_deporte():
    return [Redactores["Leo",1234], Redactores["Ana",1234],Redactores["Julia",1234]]

def main():
    jefe_redactor_entretenimiento = Jefes("Jose Quevedo", 1234,get_redactores_entreteimiento)
    jefe_redactor_farandula = Jefes("Antonio Guerra", 1234,get_redactores_farandula)
    jefe_redactor_deportes = Jefes("Luis Bello", 1234,get_redactores_deporte)

    seccion_entretenimiento = Seccion(jefe_redactor_entretenimiento)
    seccion_farandula = Seccion(jefe_redactor_farandula)
    seccion_deportes = Seccion(jefe_redactor_deportes)

main()