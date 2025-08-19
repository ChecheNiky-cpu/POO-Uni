class Persona:  
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre      # Público
        self._edad = edad         # Protegido
        self.__saldo = saldo      # Privado

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self._edad}, Saldo: {self.__saldo}")

    def cambiar_edad(self, nueva_edad):
        self._edad = nueva_edad

    def depositar(self, monto):
        self.__saldo += monto

class Empleado(Persona):
    def cumplir_anios(self):
        self._edad += 1

# ---- Menú ----
persona = Persona("Ana", 30, 1000)
empleado = Empleado("Luis", 25, 500)

while True:
    print("\n--- MENÚ ---")
    print("1) Ver datos persona")
    print("2) Cambiar nombre (público)")
    print("3) Cambiar edad (protegido)")
    print("4) Depositar saldo (privado)")
    print("5) Ver datos empleado")
    print("6) Empleado cumple años (usa protegido)")
    print("7) Intentar acceder a __saldo (mostrar error)")
    print("8) Salir")
    
    op = input("Opción: ")

    if op == "1":
        persona.mostrar_datos()
    elif op == "2":
        persona.nombre = input("Nuevo nombre: ")
    elif op == "3":
        persona.cambiar_edad(int(input("Nueva edad: ")))
    elif op == "4":
        persona.depositar(float(input("Monto a depositar: ")))
    elif op == "5":
        empleado.mostrar_datos()
    elif op == "6":
        empleado.cumplir_anios()
        print("Edad aumentada.")
    elif op == "7":
        try:
            print(persona.__saldo)  # Esto debería fallar
        except AttributeError as e:
            print("Error al acceder a __saldo:", e)
    elif op == "8":
        break
    else:
        print("Opción no válida")
