#funciona
class OPT:
    def __init__(self, Demanda, Marcos):
        self.Demanda = Demanda
        self.Marcos = Marcos
        self.Pila = []#trabaja como memoria
        self.Falla = []
        self.numeroFallos = 0
        self.n = len(self.Demanda)
        self.contadorFifo = 0
        self.anteriorSwFifo = 0

    def PilaVacia(self):
        if len(self.Pila) == 0:
            return True
        return False

    def PilaLlena(self):
        if len(self.Pila) == self.Marcos:
            return True
        return False

    def buscarReferenciaLejana(self, Di, x):
        posicion = -1; c = 0; posPila = 0
        for i in self.Pila:
            if (Di + 1 < self.n) and (i in self.Demanda[Di + 1: ]):
                if posicion == -1:
                    posicion = self.Demanda[Di + 1:].index(i)
                    posPila = c
                else:
                    cand = self.Demanda[Di + 1:].index(i)
                    if cand > posicion:
                        posicion = cand
                        posPila = c
            c += 1
        if posicion != -1:
            self.Pila[posPila] = x
            return True
        return False

    def FIFO(self, x, contador):
        if self.PilaVacia() or (not self.PilaLlena()):
            self.Pila.append(x)
        elif self.PilaLlena():
            self.Pila[contador] = x


    def OPT(self):
        Di = 0
        for x in self.Demanda:
            if self.PilaVacia() or (not self.PilaLlena() and not x in self.Pila):
                self.Pila.append(x)
                self.numeroFallos += 1
                self.Falla.append('x')
            elif self.PilaLlena():
                if x in self.Pila:
                    #si se encuentra x en la memoria + 1
                    self.Falla.append('-')
                else:
                    if self.buscarReferenciaLejana(Di, x):
                        # suponemos de que existe la referencia mas lejana aqui se hace uso
                        # del OPT
                        self.numeroFallos += 1
                        self.Falla.append('x')
                        self.anteriorSwFifo = 1
                    else:
                        # aqui se usa FIFO porque no encuentra una referencia lejana
                        if self.anteriorSwFifo:
                            self.contadorFifo = 0
                        else:
                            if self.contadorFifo + 1 < self.Marcos:
                                self.contadorFifo += 1
                            else:
                                self.contadorFifo = 0
                        self.FIFO(x, self.contadorFifo)
                        self.Falla.append('x')
                        self.numeroFallos += 1
                        self.anteriorSwFifo = 0
            Di += 1

    def mostrarFallas(self):
        print('**********************OPT****************************')
        print('D',*self.Demanda, '\n'
                                 ' ',*self.Falla, sep='  ')
        print(f'NFallos = {self.numeroFallos}\n'
              f'NBienes = {self.n - self.numeroFallos}'
              f'\n')

    def solucion(self):
        try:
           self.OPT()
           self.mostrarFallas()
        except Exception as error:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""D = [2, 3, 4, 2, 1, 3, 5, 2, 4, 3, 2, 1]
O1 = OPT(Demanda=D, Marcos=3)
O1.solucion()
D1 = [3, 2, 1, 4, 6, 5, 3, 2, 4, 3]
O2 = OPT(Demanda=D1, Marcos=4)
O2.solucion()"""
