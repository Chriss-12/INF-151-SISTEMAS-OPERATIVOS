# funciona
class FIFO1:  # PARA REEMPLAZO DE PAGINAS
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.Pila = []  # trabaja como memoria
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0

    def PilaVacia(self):
        if len(self.Pila) == 0:
            return True
        return False

    def PilaLlena(self):
        if len(self.Pila) == self.Marcos:
            return True
        return False

    def Asignacion(self, x, contador):
        self.Pila[contador] = x
        self.contadorFifo += 1

    def FIFO(self):
        for x in self.Demanda:
            if self.PilaVacia() or (not self.PilaLlena() and not x in self.Pila):
                self.Pila.append(x)
                self.numeroFallos += 1
                self.Falla.append('x')
            elif self.PilaLlena():
                if x in self.Pila:
                    # si se encuentra x en la memoria se mantiene
                    self.Falla.append('-')
                else:
                    # aqui se usa FIFO porque no encuentra una referencia lejana
                    if not self.contadorFifo < self.Marcos:
                        self.contadorFifo = 0
                    self.Asignacion(x, self.contadorFifo)
                    self.Falla.append('x')
                    self.numeroFallos += 1

    def mostrarFallas(self):
        print('**********************FIFO****************************')
        print('D', *self.Demanda, '\n'
                                  ' ', *self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
            self.FIFO()
            self.mostrarFallas()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")


"""O2 = FIFO1(Demanda=[3, 2, 1, 4, 6, 5, 3, 2, 4, 3], Marcos=4)
O2.solucion()
"""