from recordatorio import Recordatorio
from tarea import Tarea
def main():
    list_rec = []
    while True:
        option = input("Bienvenido ¿Qué deseas hacer?\n1.Crear recordatorios\n2.Eliminar recordatorios\n3. Actualizar recordatorios\n4. Ver lista de recordatorios\n5. Desplegar sistema por días\n6.Salir\n")
        if option == "1":
            list_tareas = []
            while True:
                tarea = Tarea(input("Introduzca la tarea a realizar: "))
                list_tareas.append(tarea)
                salida = input("¿Desea agregar otra tarea?\n1. Sí\n2.No\n")
                if salida == "2":
                    break
            recordatorio = Recordatorio(input("Nombre: "), input("Hora: "), input("día: "), input("mes: "), list_tareas)
            list_rec.append(recordatorio)
        if option == "2":
            i = 0
            for elemento in list_rec:
                print(i, ".")
                elemento.mostrar()
                i += 1
            delete = int(input("Introduce el número del recordatorio que deseas eliminar: "))
            list_rec.pop(delete)
            i = 0
            print("*****RECORDATORIOS RESTANTES*****")
            for elemento in list_rec:
                print(i, ".")
                elemento.mostrar()
                i+=1
        if option == "3":
            while True:
                i = 0
                for elemento in list_rec:
                    print(i, ".")
                    elemento.mostrar()
                    i+=1
                eleccion = int(input("Numero del recordatorio que deseas modificar: "))
                modificar = input("Que deseas modificar\n1. Nombre\n2. Fecha\n3. Hora\n4.Agregar o eliminar tareas\n")
                if modificar == "1":
                    list_rec[eleccion].nombre = input("Introduzca el nuevo nombre: ")
                if modificar == "2":
                    list_rec[eleccion].dia = input("Introduzca el nuevo dia: ")
                    list_rec[eleccion].mes = input("Introduzca el nuevo mes: ")
                if modificar == "3":
                    list_rec[eleccion].hora = input("Introduzca la nueva hora: ")
                if modificar == "4":
                    user = input("1.Eliminar\n2.Agregar\n")
                    if user == "1":
                        a = 0
                        for element in list_rec[eleccion].descripcion:
                            print(a, ".")
                            element.mostrarTarea()
                            a+=1
                        tarea_eliminada = int(input("Cual deseas eliminar: "))
                        list_rec[eleccion].descripcion.pop(tarea_eliminada)
                    if user == "2":
                        list_rec[eleccion].descripcion.append(Tarea(input("Introduce la nueva tarea: ")))
                salida2 = input("¿Desea modificar otra cosa?\n1. Sí\n2.No\n")
                if salida2 == "2":
                    break
                
        if option == "4":
            print("LISTA DE RECORDATORIOS")
            i = 0
            for elemento in list_rec:
                print(i, ".")
                elemento.mostrar()
                i+=1
        if option == "5":
            dia = int(input("Día de hoy: "))
            mes = int(input("Mes actual: "))
            while True:
                encontrado = False
                for elemento2 in list_rec:
                    x = elemento2.dia
                    y= elemento2.mes
                    if int(elemento2.dia) == dia or int(elemento2.mes == mes):
                        elemento2.mostrar()
                        encontrado = True
                if encontrado == False:
                    print("No hay recordatorios para este día")
                user2 = input("¿Quieres ver el siguiente día?\n1.Sí\n2.No\n")
                if user2 == "2":
                    break
                dia += 1
                

        if option == "6":
            break
main()