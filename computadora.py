class Computadora:
    def __init__(self, marca, modelo, ram):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram

        self.encendida = False

    def encender(self):

        if not self.encendida:
            self.encendida = True
            print(f"La computadora {self.marca} {self.modelo} esta encendida.")
        else:
            print("La computadora esto ya esta encendido")

    def apagar(self):

        if self.encendida:
            self.encendida = False

            print(
                f"La computadora con la marca {self.marca} {self.modelo} está apagada."
            )
        else:
            print("este computador  ya está apagada.")

    def actualizar_ram(self, nueva_ram):
        if not self.encendida:
            print(
                "Por favor, encienda la computadora antes de actualizar la RAM para evitar daños  o bugs en la ram xd."
            )
            return
        if nueva_ram > self.ram:
            print(f"Actualizando RAM de {self.ram}GB a {nueva_ram}GB.")
            self.ram = nueva_ram
        else:
            print("La nueva RAM debe ser mayor que la actual.")


mi_computadora = Computadora("Dell", "Inspiron", 8)
mi_computadora.encender()
mi_computadora.actualizar_ram(16)
mi_computadora.apagar()
