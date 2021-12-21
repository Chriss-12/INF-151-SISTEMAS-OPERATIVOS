import numpy as np
from matplotlib import pyplot as plt
class SSTF:
    def __init__(self, Peticiones, inicio):
        self.Pistas = []
        self.Peticiones = Peticiones
        self.Movimientos = 0
        self.inicio = inicio

    def graficar(self):
        self.Peticiones.insert(0, self.inicio)
        y = np.array(self.Peticiones)
        x = np.array([i for i in range(1, len(self.Peticiones) + 1)])
        plt.plot(x, y, 'og--', mfc='y', mec='y')
        plt.title('SSTF(Shortes seek time fast first)')
        plt.xlabel('Peticiones')
        plt.ylabel('Pistas')
        plt.show()

    def ordenar(self):
        auxiliar = []
        auxiliar2 = []
        for x in self.Peticiones:
            if x <= self.inicio:
                auxiliar.append(x)
            else:
                auxiliar2.append(x)
        self.Peticiones.clear()
        self.Peticiones.extend(sorted(auxiliar)[::-1])
        self.Peticiones.extend(sorted(auxiliar2))

    def SSTF(self):
        self.ordenar()
        for x in range(len(self.Peticiones)):
            if x == 0:
                self.Movimientos += abs(self.Peticiones[x] - self.inicio)
            else:
                self.Movimientos += abs(self.Peticiones[x] - self.Peticiones[x - 1])

    def solucion(self):
        try:
            self.SSTF()
            print('**********************SSTF****************************')
            print(f'numero de movimientos = {self.Movimientos}')
            self.graficar()
        except Exception:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""S1 = SSTF(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)
S1.solucion()"""