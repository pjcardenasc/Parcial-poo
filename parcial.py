class cuenta:
    def __init__(self, user, contraseña, cuenta):
        self.user = user
        self.__contraseña = contraseña
        self.cuenta = cuenta
    def crearcuenta():
        crearuser = input("Ingrese un usuario: ")
        crearcontraseña = input("Ingrese una contraseña: ")
    crearcuenta()         

class Estudiante:
    def __init__ (self, pregrado, posgrado, noactivo):
        self.pregrado = pregrado
        self.posgrado = posgrado
        self.noactivo = noactivo
    def pedirlibro():
        print("")
class Libro(Estudiante):
    def __init__ (self, historia, matematicas, ciencias, salud):
        self.historia = historia
        self.matematicas = matematicas
        self.ciencias = ciencias
        self.salud = salud
    @property
    def cantidad(self):
        historia = 5
        matematicas = 3
        ciencias = 1
        salud = 0
    def registrolibros():
        print("Seleccione uno de los libros para ver su disponibilidad: ")
        opc= input("1. Historia, 2. Matematicas, 3. Ciencias, 4. salud ")
        if (opc == 1):
            print(f"Quedan {historia} libros de historia")
        elif (opc == 2):
            print(f"Quedan {matematicas} libros de matematicas")
        elif (opc == 3):
            print(f"Quedan {ciencias} libros de ciencias")
        elif (opc == 4):
            print(f"Quedan {salud} libros de salud")
    def ingresarlibro():
        print("Ingrese el libro que quiere devolver: ")
        ingresaropc = input("1. Historia, 2. Matematicas, 3. Ciencias, 4. salud")
        if ingresaropc == 1:
            historiaw= input("Ingrese cuantos libros va a ingresar: ")
            historia += historiaw
            print(f"Usted ha ingresado {historiaw} libros de historia, ahora hay ")
        elif ingresaropc == 2:
            historiaw= input("Ingrese cuantos libros va a ingresar: ") 
            historia += historiaw  
    registrolibros()
    ingresarlibro()
