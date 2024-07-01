from cliente import Cliente
from api_estadios import ApiEstadios
from api_equipos import ApiEquipos
#from estadio import Estadio
#from equipos import Equipo
#from partidos import Partido
from api_partidos import ApiPartidos

class Creador_usuarios:
 

    def __init__(self):
   
        self.clientes = []

    def _crear_cliente(self, partidos_disponibles):
      
        cedula = input("Escriba su cédula: ")
        while not cedula.isnumeric():
            print("Error, debe ingresar solo números.")
            cedula = input("Escriba su cédula: ")

        nombre = input("Escriba su nombre: ")
        while not (nombre.replace(" ", "").isalpha()):  # Permitir espacios en el nombre
            print("Error, debe ingresar solo letras.")
            nombre = input("Escriba su nombre: ")

        edad = input("Cuántos años tienes: ")
        while not edad.isnumeric():
            print("Error, debe ingresar solo números.")
            edad = input("Cuántos años tienes: ")
            
        print("Partidos disponibles:")
        for i, partido in enumerate(partidos_disponibles):
            print(f"{i+1}. {partido}")
        partido_index = int(input("Elija el partido (número): ")) - 1
        partido = partidos_disponibles[partido_index]

        tipo_entrada = input("Escriba el tipo de entrada (General o Vip): ")
        while tipo_entrada != "General" and tipo_entrada != "Vip":
            print("Error, escribiste algo mal.")
            tipo_entrada = input("Escriba el tipo de entrada (General o Vip): ")
            
        cliente = Cliente(nombre, cedula, edad, partido, tipo_entrada)
        self.clientes.append(cliente)

        print("Cliente creado con éxito!")
        print("Nombre:", cliente.nombre)
        print("Cedula:", cliente.cedula)
        print("Edad:", cliente.edad)
        print("Partido:", cliente.partido)
        print("Tipo de entrada:", cliente.tipo_entrada)

        return self.clientes


