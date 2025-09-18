from Contraseña import Contraseña 

class Persona:
    def __init__(self, nombre, edad, genero, peso, estatura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.estatura = estatura
        self.contraseña = Contraseña(8)
    
    #Funcion calcular IMC    
    def calcular_imc(self):
        imc = self.peso / ((self.estatura/100)**2)
        print(f"El IMC de {self.nombre} es de {imc:.2f}")
        
    #Funcion verificar +18 años
    def verificar_mayoria_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad, tiene {self.edad} años")
        else:
            print(f"{self.nombre} no es mayor de edad, tiene {self.edad} años")
        
    #Funcion mostrar contraseña
    def mostrar_contraseña(self):
        print(f"La contraseña asignada a {self.nombre} es: {self.contraseña.contraseña}")


#Funcion crear objeto Persona
def crear_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    genero = input("Ingrese el genero de la persona: ")
    peso = float(input("Ingrese el peso de la persona (En kg): "))
    estatura = int(input("Ingrese la estatura de la persona (En cm): "))
    return Persona(nombre, edad, genero, peso, estatura)


#Funcion Menú Principal
def menu_principal():
    personas = []
    while True:
        print("\nMenú Principal\n")
        print("1. Crear persona")
        print("2. Calcular IMC de la persona")
        print("3. Verificar mayoria de edad")
        print("4. Consultar contraseña")
        print("5. Verificar contraseña")
        print("6. Salir del programa")
        
        opcion_elegida = int(input("Por favor ingrese la Opción que desee: "))

        #verificar si la opcion es valida
        while opcion_elegida < 1 or opcion_elegida > 6:
            print("Opción inválida. Por favor intente nuevamente: ")
            opcion_elegida = int(input())
            
        #ejecucion de la funcion para crear persona
        if opcion_elegida == 1:
            persona = crear_persona()
            personas.append(persona)
            print(f"Persona {persona.nombre} registrada con éxito. Su contraseña asignada es: {persona.contraseña.contraseña}")

        #ejecucion de la funcion para calcular IMC de la persona
        elif opcion_elegida == 2:
            if not personas:
                print("\nNo hay ninguna persona registrada.")
            else:
                print("\nSeleccione una persona para calcular IMC:")
                for i, p in enumerate(personas, start=1):
                    print(f"{i}. {p.nombre}")
                eleccion = int(input("Ingrese el número: "))
                if eleccion < 1 or eleccion > len(personas):
                    print("Opción inválida.") 
                else:
                    personas[eleccion-1].calcular_imc()
                    
        #ejecucion de la funcion para verificar mayoria de dad
        elif opcion_elegida == 3:
            if not personas:
                print("\nNo hay ninguna persona registrada.")
            else:
                print("\nSeleccione una persona para verificar mayoría de edad:")
                for i, p in enumerate(personas, start=1):
                    print(f"{i}. {p.nombre}")
                eleccion = int(input("Ingrese el número: "))
                if eleccion < 1 or eleccion > len(personas):
                    print("Opción inválida.")
                else:
                    personas[eleccion-1].verificar_mayoria_edad()

        #ejecucion de la funcion para mostrar contraseña
        elif opcion_elegida == 4:
            if not personas:
                print("\nNo hay ninguna persona registrada.")
            else:
                print("\nSeleccione una persona para mostrar su contraseña:")
                for i, p in enumerate(personas, start=1):
                    print(f"{i}. {p.nombre}")
                eleccion = int(input("Ingrese el número: "))
                if eleccion < 1 or eleccion > len(personas):
                    print("Opción inválida.")
                else:
                    personas[eleccion-1].mostrar_contraseña()

        #ejecucion de la funcion para verificar contraseña
        elif opcion_elegida == 5:
            if not personas:
                print("\nNo hay ninguna persona registrada.")
            else:
                print("\nSeleccione una persona para verificar su contraseña:")
                for i, p in enumerate(personas, start=1):
                    print(f"{i}. {p.nombre}")
                eleccion = int(input("Ingrese el número: "))
                if eleccion < 1 or eleccion > len(personas):
                    print("Opción inválida.")
                else:
                    persona = personas[eleccion-1]
                    if persona.contraseña.verificar_seguridad_contraseña():
                        print(f"La contraseña de {persona.nombre} es segura")
                    else:
                        print(f"La contraseña de {persona.nombre} NO es segura")

        #ejecucion de la funcion para salir del programa
        elif opcion_elegida == 6:
            print("Saliendo del programa...")
            break


#Ejecución main y ejecucion menu principal
def main():
    menu_principal()

if __name__ == "__main__":
    main()




