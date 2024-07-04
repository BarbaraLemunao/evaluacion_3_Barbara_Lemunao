import csv 

class datos_jugador:
        def __init__(self ,nombre_jugador , año_nacimiento, equipo):
            self.nombre_jugador = nombre_jugador
            self.año_nacimiento = año_nacimiento
            self.equipo = equipo

        equipos = ["usa", "mexico", "colombia"]
        bitacoras = []
        jugadores = []
        def registrar_jugador():
            jugador = input("Ingrese el nombre del jugador: ")
            año_nacimiento= int(input("Ingrese el año de nacimiento: "))
            equipo = str(input("ingrese el nombre de su equipo: ","usa", "Mexico", "colombia"))
            cant_goles = int(input("Ingrese la cantidad de goles: "))

        def registrar_goles():
            equipo = str(input("Ingrese el nombre de su equipo: " ,["usa", "mexico", "colombia"] ))
            cant_goles = int(input("Ingrese la cantidad de goles: "))
        
        def listar_bitacoras():
             if not bitacoras:
                  print("no hay registro de bitacoras")
             else:
                  for idx, jugador in enumerate(jugador, start=1):
                       print(f"jugador
                             {idx}: {jugador}")
        
        def imprimir_bitacora():
             
        id_bitacora = 0000

        def id_bitacora():
             
        
             

        opcion = input("ingrese la opcion que desea realizar: ")

        if opcion == "!":
             registrar_jugador ()
        elif opcion == "2" :
             listar_bitacoras ()
        elif opcion == "3" :
             imprimir_bitacora ()
        elif opcion == "4" :
             id_bitacora ()
        elif opcion == "5" :
             print("gracias por su visita")
             break
        else:
             print("opcion invalida , intentelo nuevamente.")

                       
        
                       

             

        

