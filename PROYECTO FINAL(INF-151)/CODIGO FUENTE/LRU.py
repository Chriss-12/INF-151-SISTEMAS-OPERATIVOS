#funciona
class LRU:
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.PilaMemoria = []#la memoria
        self.Pila = []#la pila que servira para hacer el reemplazo
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0

    def PilaVacia(self, Pila):
        if len(Pila) == 0:
            return True
        return False

    def PilaLlena(self, Pila):
        if len(Pila) == self.Marcos:
            return True
        return False

    def PilaSubirElemento(self, x):
        elem = self.Pila.pop(self.Pila.index(x))
        self.Pila.append(elem)

    def PilaApilarElemento(self, x):
        reemplazar = self.Pila.pop(0)
        self.Pila.append(x)
        self.PilaMemoria[self.PilaMemoria.index(reemplazar)] = x

    def LRU(self):
        for x in self.Demanda:
            if self.PilaVacia(self.PilaMemoria) or (not self.PilaLlena(self.PilaMemoria)):
                self.PilaMemoria.append(x)
                self.Pila.append(x)
                self.Falla.append('x')
                self.numeroFallos += 1
            else:
                if x in self.PilaMemoria:
                    self.Falla.append('-')
                    self.PilaSubirElemento(x)
                else:
                    self.PilaApilarElemento(x)
                    self.Falla.append('x')
                    self.numeroFallos += 1

    def mostrarFallas(self):
        print('**********************LRU****************************')
        print('D',*self.Demanda, '\n'
                                 ' ',*self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
           self.LRU()
           self.mostrarFallas()
           print(self.PilaMemoria)
           print(self.Pila)
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""L1 = LRU(Demanda=[2, 4, 6, 2, 3, 4, 5, 2, 1, 2, 3, 4], Marcos=3)
L1.solucion()"""
