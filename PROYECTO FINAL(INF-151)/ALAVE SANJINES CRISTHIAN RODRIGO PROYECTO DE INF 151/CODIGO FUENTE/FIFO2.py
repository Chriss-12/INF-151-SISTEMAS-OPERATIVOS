import numpy as np
from matplotlib import pyplot as plt
class FIFO2:
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
        plt.title('FIFO')
        plt.xlabel('Peticiones')
        plt.ylabel('Pistas')
        plt.show()

    def FIFO(self):
        for x in range(len(self.Peticiones)):
            if x == 0:
                self.Movimientos += abs(self.Peticiones[x] - self.inicio)
            else:
                self.Movimientos += abs(self.Peticiones[x] - self.Peticiones[x - 1])

    def solucion(self):
        try:
            self.FIFO()
            print('**********************FIFO****************************')
            print(f'numero de movimientos = {self.Movimientos}')
            self.graficar()
        except Exception:
            print("OCURRIO ALGUN ERROR INESPERADO!!!")

"""FF21 = FIFO2(Peticiones=[10, 40, 5, 20, 15, 35, 40, 5, 10, 25, 10, 35, 10, 5, 20], inicio=20)
FF21.solucion()"""