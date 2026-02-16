class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0
    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50
    def invertir(self):
        self.dinero += 20
    def ahorrar(self):
        self.dinero += 20
    def trabajar(self):
        self.dinero += 15
    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10
jugador = HijoProdigo(input("Ingrese su nombre: "))
print(f"{jugador.nombre} ha recibido su herencia, tiene {jugador.dinero} de dinero, {jugador.dignidad} de dignidad, y {jugador.hambre} de hambre.")
while jugador.dinero > 0:
    print(f"Sigues viviendo lejos de casa... Tu dinero es {jugador.dinero}")
    jugador.gastar_todo()
    jugador.reflexionar()
print("El dinero se acabó")
print(f"Su nivel de arrepentimiento está en {jugador.arrepentimiento}")
opcion = int(input("Elige una opción:\n1. Gastar todo\n2. Invertir\n3. Ahorrar\n"))
if opcion == 1:
    jugador.gastar_todo()
elif opcion == 2:
    jugador.invertir()
elif opcion == 3:
    jugador.ahorrar()
else:
    print("Opción inválida")
