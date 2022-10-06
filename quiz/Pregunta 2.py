# Nombre del estudiante : Paula Alonso
#Número de carnet : 20221110206
#Correo unimet: paula.alonso@correo.unimet.edu.ve
anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}
print("¡Bienvenido a Anime-Te-ve!")
option = ""
registro = []
while option != "3":
    option = input("¿Qué deseas hacer? Selecciona el número que corresponda:\n1. Seleccionar serie\n2. Consultar historial de vistas\n3. Salir\n")
    if option == "1":
        for serie, info in anime.items():
            print(serie)
        anime_user = input("¿Qué anime deseas ver? Escribe el nombre de la opción que corresponda: ")
        anime_choosed = anime.get(anime_user)
        for temporada in anime_choosed:
            print(temporada)
        temporadas= input("Introduzca el número que corresponda a la temporada deseada")
        temporada_choosed = anime_choosed.get(temporadas)
        for caps in temporada_choosed:
            for x, other in caps.items():
                capitulo = caps.get("cap")
                name = caps.get("name")
                duration = caps.get("duration")
            print(f"Capítulo: {capitulo}, Nombre: {name}, Duración {duration}")
        capitulo_user = input("Introduzca el número del capítulo que desea: ")
        elección = ""
        for caps in temporada_choosed:
            for x, other in caps.items():
                capitulo = caps.get("cap")
                name = caps.get("name")
                duration = caps.get("duration")
                if capitulo == capitulo_user:
                    elección = {"Capítulo" : capitulo, "Nombre": name, "Duración": duration}
                    break
        registro.append(elección)
        if option == "2": 
            print(registro)
        
        
        


        
        
        
