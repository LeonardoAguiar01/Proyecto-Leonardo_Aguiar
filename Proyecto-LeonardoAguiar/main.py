from api_equipos import ApiEquipos
from api_estadios import ApiEstadios
from api_partidos import ApiPartidos
from gestion_partidos import Gestion_partidos
from guardar_clientes import Creador_usuarios

class Main():
    
    def __init__(self):
        self.gestion_partidos = Gestion_partidos()
        self.creador_usuarios = Creador_usuarios()  
    
    def mostrar_menu(self):
        print('-- Bienvenido a Eurocopa 2024')
        while True:
            print('''
    1. Gestión de partidos y estadios
    2. Gestión de venta de entradas
    3. Gestión de asistencia a partidos
    4. Gestión de restaurantes
    5. Gestión de venta de restaurantes
    6. Indicadores de gestión 
    =========================
    7. Salir
    ''')
                
            seleccion = input("Ingrese el número correspondiente a su selección: ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1, 8):
                print('Error: Selección inválida')
                seleccion = input("Ingrese el número correspondiente a su selección: ")

            if seleccion == '1':
                self.gestion_partidos.main()
            elif seleccion == '2':
                self.crear_usuario_menu()
            elif seleccion == '3':
                print("Opción en construcción: Gestión de asistencia a partidos")
            elif seleccion == '4':
                print("Opción en construcción: Gestión de restaurantes")
            elif seleccion == '5':
                print("Opción en construcción: Gestión de venta de restaurantes")
            elif seleccion == '6':
                print("Opción en construcción: Indicadores de gestión")
            else:
                print('Gracias por su visita. Vuelva pronto...')
                break

            ans = input('¿Desea continuar? [y/n]: ')
            while ans.lower() not in ['y', 'n']:
                print('Respuesta inválida')
                ans = input('¿Desea continuar? [y/n]: ')
                
            if ans == 'n':
                print('Gracias por su visita. Vuelva pronto...')
                break

    def crear_usuario_menu(self):
        """
        Método para gestionar la creación de usuarios y venta de entradas.
        """
        print('Gestión de venta de entradas')
        partidos_disponibles = [str(partido) for partido in ApiPartidos.partidos]  # Obtén los nombres de los partidos disponibles
        self.creador_usuarios._crear_cliente(partidos_disponibles)  # Llama al método de Creador_usuarios

if __name__ == '__main__':
    print('=== Sistema de Gestión Eurocopa 2024 ===')
    ApiEquipos.cargar_equipos('equipos.txt')
    ApiEstadios.cargar_estadios('estadios.txt')
    ApiPartidos.cargar_partidos('partidos.txt')
    main = Main()
    main.mostrar_menu()
