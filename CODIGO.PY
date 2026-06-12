from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, nombre, edad, peso):
        self._nombre = nombre
        self._edad = edad
        self._peso = peso

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_peso(self):
        return self._peso

    @abstractmethod
    def hacer_ruido(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre, edad, peso, raza):

        super().__init__(nombre, edad, peso)
        self._raza = raza 

    def get_raza(self):
        return self._raza

    def hacer_ruido(self):
        return "¡Guau, guau!"


class Gato(Mascota):
    def __init__(self, nombre, edad, peso, tipo_pelo):
        super().__init__(nombre, edad, peso)
        self._tipo_pelo = tipo_pelo 

    def get_tipo_pelo(self):
        return self._tipo_pelo

    def hacer_ruido(self):
        return "¡Miau, miau!"

class Veterinario:
    def __init__(self, nombre, especialidad):
        self._nombre = nombre
        self._especialidad = especialidad

    def obtener_datos_vet(self):
        return f"Dr. {self._nombre} (Especialidad: {self._especialidad})"


class Consulta:
    def __init__(self, mascota, veterinario, motivo):
        self._mascota = mascota
        self._veterinario = veterinario
        self._motivo = motivo

    def calcular_precio(self):
        precio_fijo = 15000

        if self._mascota.get_peso() > 15:
            return precio_fijo + 5000
        else:
            return precio_fijo

def menu_principal():
    mis_mascotas = []
    mis_consultas = []

    vet_de_turno = Veterinario("Juaquín Díaz", "Perros y Gatos")

    ejecutando = True
    while ejecutando:
        print("\nMENÚ VETERINARIA")
        print("1. Registrar una mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Crear una consulta médica (Calcular Costo)")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nREGISTRAR MASCOTA")
            tipo = input("¿Es un Perro (P) o un Gato (G)?: ").upper()
            nombre = input("Nombre: ")
            edad = int(input("Edad en años: "))
            peso = float(input("Peso en kilos: "))

            if tipo == "P":
                raza = input("Raza del perro: ")
                nuevo_perro = Perro(nombre, edad, peso, raza)
                mis_mascotas.append(nuevo_perro)
                print("¡Perro registrado con éxito!")
            elif tipo == "G":
                pelo = input("Tipo de pelo (largo/corto): ")
                nuevo_gato = Gato(nombre, edad, peso, pelo)
                mis_mascotas.append(nuevo_gato)
                print("¡Gato registrado con éxito!")
            else:
                print("Opción no válida. Intenta otra vez.")

        elif opcion == "2":
            print("\nLISTA DE MASCOTAS")
            if len(mis_mascotas) == 0:
                print("No hay ninguna mascota registrada en el sistema.")
            else:
                for posicion, mascota in enumerate(mis_mascotas, start=1):
                    print(f"{posicion}) Nombre: {mascota.get_nombre()} | Edad: {mascota.get_edad()} años | Peso: {mascota.get_peso()}kg")

        elif opcion == "3":
            print("\nCREAR CONSULTA")
            if len(mis_mascotas) == 0:
                print("Primero debes registrar una mascota en la opción 1.")
            else:
                print("Selecciona qué mascota va al doctor:")
                for posicion, mascota in enumerate(mis_mascotas, start=1):
                    print(f"{posicion}- {mascota.get_nombre()}")
                
                elegido = int(input("Ingresa el número de la mascota: ")) - 1

                if 0 <= elegido < len(mis_mascotas):
                    mascota_elegida = mis_mascotas[elegido]
                    motivo_visita = input("¿Por qué viene a la veterinaria?: ")

                    nueva_cita = Consulta(mascota_elegida, vet_de_turno, motivo_visita)
                    mis_consultas.append(nueva_cita)
                    
                    print("\nBOLETA DE ATENCIÓN")
                    print(f"Paciente: {mascota_elegida.get_nombre()}")
                    print(f"Atendido por: {vet_de_turno.obtener_datos_vet()}")
                    print(f"Motivo: {motivo_visita}")
                    print(f"Sonido del animal: {mascota_elegida.hacer_ruido()}") 
                    print(f"Total a pagar: ${nueva_cita.calcular_precio()}")
                else:
                    print("Número incorrecto. Volviendo al menú.")

        elif opcion == "4":
            print("Cerrando el sistema de veterinaria. ¡Adiós!")
            ejecutando = False
        else:
            print("Opción incorrecta, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()